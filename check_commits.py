import datetime
from github import Github
from dotenv import load_dotenv
import os

load_dotenv()

github_token = os.getenv("GITHUB_TOKEN")

g = Github(github_token)

user = g.get_user()
print(f"Authenticated as {user.login}")

repo_name = "minnathdhani/Devops_pipeline" 
repo = g.get_repo(repo_name)

latest_commit = repo.get_commits()[0]
latest_commit_date = latest_commit.commit.committer.date

stored_date_str = "2025-02-15T12:00:00Z"
stored_date = datetime.fromisoformat(stored_date_str[:-1]) 

if latest_commit_date > stored_date:
    print("There is a new commit.")
else:
    print("No new commits.")