# Use the official MySQL image
FROM mysql:5.7

# Set environment variables to configure MySQL
ENV MYSQL_ROOT_PASSWORD=Rum8&Tag2
ENV MYSQL_DATABASE=panoptesdb
ENV MYSQL_USER=teamAdmin
ENV MYSQL_PASSWORD=NookBrosGotchu

# Optional: Copy custom MySQL configuration
COPY my.cnf /etc/mysql/conf.d/

# Optional: Initialization scripts
COPY init.sql /docker-entrypoint-initdb.d/

# When using Dockerfile, no CMD is needed because the base image handles it
