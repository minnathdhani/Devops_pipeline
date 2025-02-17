import requests
import os
import subprocess

# GitHub repository details
GITHUB_REPO = "minnathdhani/Devops_pipeline"
GITHUB_BRANCH = "main"
LOCAL_REPO_PATH = "/var/www/html"
LAST_COMMIT_FILE = "/tmp/last_commit.txt"
GITHUB_API_URL = f"https://github.com/minnathdhani/Devops_pipeline.git"