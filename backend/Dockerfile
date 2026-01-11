FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# SQLite DB will live in /data (mounted volume)
ENV DB_PATH=/data/blog.db

EXPOSE 5000
CMD ["python", "app.py"]
