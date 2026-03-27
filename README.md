# GitHub Cloud Connector

## Objective
A FastAPI-based connector to interact with GitHub APIs.

---

## Setup

1. Open command prompt and run:
```

git clone <repo-url>

```

2. Navigate to the project folder:
```

cd github-connector

```

3. Install required dependencies:
```

pip install -r requirements.txt

```

4. Create a `.env` file to store the Personal Access Token:
```

GITHUB_TOKEN=your_token_here

```

---

## Run Project

Use the below command to run the project:
```

uvicorn app.main:app --reload

```

---

## API Documentation

Swagger UI:
```

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

```

---

## API Endpoints

### 1. Get Public Repositories
```

GET /repos/{username}

```
Provide GitHub username to fetch all public repositories.

---

### 2. Get My Repositories (Private + Public)
```

GET /my-repos?visibility=all|public|private

```
Choose visibility to fetch public, private, or all repositories.

---

### 3. Create Issue
```

POST /create-issue

```
Create an issue in a repository.

**Parameters:**
- owner → GitHub username  
- repo → Repository name  
- title → Issue title  
- body → Issue description  

---

### 4. List Issues
```

GET /list-issues?owner=<owner>&repo=<repo>

```
Provide repository owner and repo name to fetch issues.

---

### 5. Get Commits
```

GET /commits?owner=<owner>&repo=<repo>

```
Fetch commit history of a repository.

---

### 6. Create Pull Request
```

POST /create-pr

```
Create a pull request from one branch to another.

**Parameters:**
- owner → GitHub username  
- repo → Repository name  
- title → PR title  
- body → PR description  
- head → Source branch (e.g., feature-branch)  
- base → Target branch (e.g., main)  

---

## Note

- `.env` file is not included for security  
- Token must have `repo` permission  
- Pull request requires two different branches (head ≠ base)
---
```

