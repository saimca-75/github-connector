import requests
from app.config import GITHUB_TOKEN, BASE_URL

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

# 🔹 1. Get authenticated user repos (public + private)
def get_my_repositories(visibility):
    visibility = visibility.lower()
    url = f"{BASE_URL}/user/repos"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return {"error": response.json()}

    repos = response.json()

        # 🔥 Apply filtering
    if visibility == "public":
        repos = [r for r in repos if not r["private"]]
    elif visibility == "private":
        repos = [r for r in repos if r["private"]]

    return [
        {
            "name": repo["name"],
            "url": repo["html_url"],
            "private": repo["private"]
        }
        for repo in repos
    ]


# 🔹 2. Get public repos of any user
def get_public_repositories(username):
    url = f"{BASE_URL}/users/{username}/repos"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return {"error": response.json()}

    return response.json()


# 🔹 3. Create issue
def create_issue(owner, repo, title, body):
    url = f"{BASE_URL}/repos/{owner}/{repo}/issues"

    data = {
        "title": title,
        "body": body
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code != 201:
        return {"error": response.json()}

    return response.json()

# 🔹 3. list issues
def list_issues(owner, repo):
    url = f"{BASE_URL}/repos/{owner}/{repo}/issues"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return {"error": response.json()}

    issues = response.json()

    return [
        {
            "title": issue["title"],
            "url": issue["html_url"],
            "state": issue["state"]
        }
        for issue in issues
    ]