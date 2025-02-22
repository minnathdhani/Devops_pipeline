#!/bin/bash

# Get the current user's home directory
USER_HOME=$(eval echo ~$(whoami))
REPO_DIR="$USER_HOME/Devops_CICD/Devops_pipeline"
PROJECT_DIR="$USER_HOME/Devops_CICD"

# Log start
echo "Starting deployment at $(date)" >> $PROJECT_DIR/log/deploy.log

# Pull latest changes
if [ -d ".git" ]; then
    cd $REPO_DIR
    git pull origin main
else
    cd $PROJECT_DIR
    git clone https://github.com/minnathdhani/Devops_pipeline.git $PROJECT_DIR > /dev/null 2>&1
fi

# Restart Nginx
sudo systemctl restart nginx

# Log completion
echo "Deployment completed at $(date)" >> $PROJECT_DIR/log/deploy.log