Project 5- A simple blog API(Flask+SQLite+ Docker)
Overview
This project is a simple blog backend API built with Flask and SQLite, fully containerized using Docker.

The SQLite database file is stored in a Docker volume to ensure data persistence across container restarts.
The application runs on a custom Docker network and the Docker image is pushed to Docker Hub.

 Requirements Met
	•	Flask Backend API 
	•	SQLite database 
	•	Database file stored in Docker volume 
	•	Custom Docker network 
	•	Full documentation 
	•	Docker image pushed to Docker Hub
  Technologies Used
	•	Python
	•	Flask
	•	SQLite
	•	Docker
	•	Docker Compose
Project Structure
project5-simple-blog/
├── backend/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yml
├── README.md
└── screenshots/
How to Run the Application
docker compose up -d --build
Verify container is running
docker compose ps
Application Access
The API runs on
http://localhost:5000
Health check:
{"status":"ok","db_path":"/data/blog.db"}
expected Response:
{"status":"ok","db_path":"/data/blog.db"}
API endpoints:
Create a blog post:
curl -X POST http://localhost:5000/posts \
  -H "Content-Type: application/json" \
  -d '{"title":"My first post","content":"Hello from SQLite volume!"}'
  List all post:
  curl http://localhost:5000/posts
  Get a single post:
  curl http://localhost:5000/posts/1
  Update a post:
  curl -X PUT http://localhost:5000/posts/1 \
  -H "Content-Type: application/json" \
  -d '{"title":"Updated title","content":"Updated content"}'
  Delete a post:
  curl -X DELETE http://localhost:5000/posts/1
  Database persistence( Docker Volume)
  The SQLite database file is stored in a Docker volume called blogdata.

Persistence test steps:
1, Create a blog post
2. Stop containers
docker compose down
start containers again:
docker compose up -d
list posts:
curl http://localhost:5000/posts
The data remains ,  proving persistence via Docker volume
Docker Network
•	Custom Docker network: blognet
	•	Allows isolated container networking
  verify:
  docker network ls
  Docker Hub
  Docker image pushed to Docker Hub:
  euniceo/project5-blog-api:latest
  Build and push commands used:
  docker build -t euniceo/project5-blog-api:latest ./backend
docker push euniceo/project5-blog-api:latest
Screenshots contains evidence of:
The screenshots/ directory contains evidence of:
	•	Running container (docker compose ps)
	•	Custom network (docker network ls)
	•	Docker volume (docker volume ls)
	•	API requests (create/list posts)
	•	Data persistence after restart
	•	Docker Hub image
  Conclusion

This project demonstrates how to build a containerized backend API with persistent storage using Docker volumes and custom networking. It follows best practices for containerization and documentation.
Author
Eunice Olajumoke

  
