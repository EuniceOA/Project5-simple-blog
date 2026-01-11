# Assignment 5 — Simple Blog (Flask + SQLite + Docker)

## Overview
A simple blog backend API built with Flask. Posts are stored in an SQLite database file that is persisted using a Docker volume. The container runs on a custom Docker network.

## Requirements Met
- Flask Backend API ✅
- SQLite database ✅
- Database file stored in volume ✅
- Custom Docker network ✅
- Documentation ✅
- Image pushed to Docker Hub ✅

## API Endpoints
- GET /health
- GET /posts
- GET /posts/<id>
- POST /posts
- PUT /posts/<id>
- DELETE /posts/<id>

## Run locally (Docker Compose)
```bash
docker compose up -d --build
