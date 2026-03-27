from fastapi import APIRouter
from app.github_service import list_issues
from app.github_service import (
    get_my_repositories,
    get_public_repositories,
    create_issue
)

router = APIRouter()

# Public repos
@router.get("/repos/{username}")
def fetch_public_repos(username: str):
    return get_public_repositories(username)

# Private + Public (authenticated)
@router.get("/my-repos")
def fetch_my_repos(visibility: str = "all"):
    return get_my_repositories(visibility)

# Create issue
@router.post("/create-issue")
def create_issue_api(owner: str, repo: str, title: str, body: str):
    return create_issue(owner, repo, title, body)

# list issues
@router.get("/list-issues")
def list_issues_api(owner: str, repo: str):
    return list_issues(owner, repo)
