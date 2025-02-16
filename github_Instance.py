from github import Github
from dotenv import load_dotenv
import os

load_dotenv()

github_token = os.getenv("GITHUB_TOKEN")

g = Github(github_token)

user = g.get_user()
print(f"Authenticated as {user.login}")

# List all repositories
print("Repositories:")
repos = user.get_repos()
for repo in repos:
    print(f"- {repo.name}")

