#!/bin/bash
# Stop and remove the existing container
if docker ps -a | grep -q proj_dev_db; then
    docker stop proj_dev_db
    docker rm proj_dev_db
fi

# Build and run the new Docker container
docker build -t proj_dev_db .
docker run --name proj_dev_db -p 3306:3306 -d proj_dev_db

# Wait for the container to be ready
sleep 30

# Execute additional MySQL commands, correctly handle the password
docker exec proj_dev_db mysql -u root -p'Rum8&Tag2' -e "CREATE DATABASE newdatabase;"
docker exec proj_dev_db mysql -u root -p'Rum8&Tag2' -e "GRANT ALL PRIVILEGES ON newdatabase.* TO 'newuser'@'localhost' IDENTIFIED BY 'user_password';"
