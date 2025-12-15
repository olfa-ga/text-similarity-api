# Text Similarity API

[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)  
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-green)](https://fastapi.tiangolo.com/)  
[![Docker](https://img.shields.io/badge/Docker-20.10-blue?logo=docker)](https://www.docker.com/)  
[![License](https://img.shields.io/badge/license-MIT-lightgrey)](LICENSE)  

 

---

## Description

**Text Similarity API** is a RESTful API built with **FastAPI** to compute semantic similarity between two texts using **Sentence Transformers**.  

Key features:  
- Compute semantic similarity with `all-MiniLM-L6-v2`.  
- Simple REST API with FastAPI.  
- Dockerized for easy deployment and development.  

---
Usage

Run locally
uvicorn app.main:app --reload

API Endpoints

GET / → Check API status

{"message": "Text Similarity API is running"}


POST /detect → Compute text similarity

Request Body:

{
  "text1": "First text",
  "text2": "Second text"
}


Response:

{
  "similarity": 0.82,
  "is_similar": true
}

Using Docker
Build Docker image
docker build -t text-similarity-api .

Run container
docker run -p 8000:8000 text-similarity-api


Or using docker-compose:

docker-compose up --build

Notes

*Default similarity threshold: 0.7 (adjustable in compute_similarity).

*Empty strings return an error.

*Docker allows hot-reload with mounted volumes for easy development.


