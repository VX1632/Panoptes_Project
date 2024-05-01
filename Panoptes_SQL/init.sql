-- Create the database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS panoptesdb;
USE panoptesdb;

-- Create a 'users' table if it doesn't already exist
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Insert a default user into the 'users' table
INSERT INTO users (username, password) VALUES ('admin', 'n0tDefau1t');

-- Create an 'events' table if it doesn't already exist
CREATE TABLE IF NOT EXISTS events (
    id INT AUTO_INCREMENT PRIMARY KEY,
    event_name VARCHAR(255) NOT NULL,
    date DATE,
    time TIME,
    event_duration INT,
    comments TEXT
);
