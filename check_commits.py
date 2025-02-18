from github import Github
from dotenv import load_dotenv
import os

load_dotenv(".env")

github_token = os.getenv("GITHUB_TOKEN")

g = Github(github_token)

user = g.get_user()
print(f"Authenticated as {user.login}")


repo_name = "minnathdhani/Devops_pipeline" 
repo = g.get_repo(repo_name)

print(f"\nCommits in repository '{repo_name}':")
commits = repo.get_commits()
for commit in commits:
    print(f"- {commit.sha}: {commit.commit.message} (by {commit.commit.author.name})")