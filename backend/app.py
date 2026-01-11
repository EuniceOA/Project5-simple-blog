from flask import Flask, request, jsonify
import os
import sqlite3
from datetime import datetime

app = Flask(__name__)

DB_PATH = os.getenv("DB_PATH", "/data/blog.db")

def get_conn():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TEXT NOT NULL
        );
    """)
    conn.commit()
    conn.close()

@app.get("/health")
def health():
    return jsonify({"status": "ok", "db_path": DB_PATH})

@app.get("/posts")
def list_posts():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, title, content, created_at FROM posts ORDER BY id DESC;")
    posts = [dict(row) for row in cur.fetchall()]
    conn.close()
    return jsonify(posts)

@app.get("/posts/<int:post_id>")
def get_post(post_id: int):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, title, content, created_at FROM posts WHERE id = ?;", (post_id,))
    row = cur.fetchone()
    conn.close()
    if row is None:
        return jsonify({"error": "Post not found"}), 404
    return jsonify(dict(row))

@app.post("/posts")
def create_post():
    data = request.get_json(silent=True) or {}
    title = (data.get("title") or "").strip()
    content = (data.get("content") or "").strip()

    if not title or not content:
        return jsonify({"error": "title and content are required"}), 400

    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO posts (title, content, created_at) VALUES (?, ?, ?);",
        (title, content, datetime.utcnow().isoformat() + "Z"),
    )
    conn.commit()
    post_id = cur.lastrowid
    conn.close()

    return jsonify({"id": post_id, "title": title, "content": content}), 201

@app.put("/posts/<int:post_id>")
def update_post(post_id: int):
    data = request.get_json(silent=True) or {}
    title = (data.get("title") or "").strip()
    content = (data.get("content") or "").strip()

    if not title or not content:
        return jsonify({"error": "title and content are required"}), 400

    conn = get_conn()
    cur = conn.cursor()
    cur.execute("UPDATE posts SET title = ?, content = ? WHERE id = ?;", (title, content, post_id))
    conn.commit()
    updated = cur.rowcount
    conn.close()

    if updated == 0:
        return jsonify({"error": "Post not found"}), 404

    return jsonify({"id": post_id, "title": title, "content": content})

@app.delete("/posts/<int:post_id>")
def delete_post(post_id: int):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM posts WHERE id = ?;", (post_id,))
    conn.commit()
    deleted = cur.rowcount
    conn.close()

    if deleted == 0:
        return jsonify({"error": "Post not found"}), 404

    return jsonify({"deleted": True, "id": post_id})

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
