#!/bin/bash

# Get the current user's home directory
USER_HOME=$(eval echo ~$(whoami))
PROJECT_DIR="$USER_HOME/Devops_pipeline/log"

# Log start
echo "Starting deployment at $(date)" >> $PROJECT_DIR/deploy.log

# Change to project directory
cd $PROJECT_DIR

# Pull latest changes
if [ -d ".git" ]; then
    git pull origin main
else
    git clone https://github.com/minnathdhani/Devops_pipeline.git $PROJECT_DIR
fi

# Restart Nginx
sudo systemctl restart nginx

# Log completion
echo "Deployment completed at $(date)" >> $PROJECT_DIR/deploy.log