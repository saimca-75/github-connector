# GitHub Cloud Connector

## Objective
A FastAPI-based connector to interact with GitHub APIs.

---

## Setup

git clone <repo-url>
cd github-connector

pip install -r requirements.txt

Create a `.env` file:

GITHUB_TOKEN=your_token_here

---

## Run Project

uvicorn app.main:app --reload

---

## API Documentation
Swagger UI:
http://127.0.0.1:8000/docs

---

## API Endpoints

### 1. Get Public Repositories
GET /repos/{username}

---

### 2. Get My Repositories
GET /my-repos?visibility=all|public|private

---

### 3. Create Issue
POST /create-issue

Parameters:
- owner
- repo
- title
- body

---

### 4. List Issues
GET /list-issues?owner=<owner>&repo=<repo>