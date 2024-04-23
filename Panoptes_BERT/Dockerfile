# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /app

# Install necessary Debian packages for Tesseract and other dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    git \
    default-libmysqlclient-dev \
    tesseract-ocr \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install additional libraries for deep learning
RUN pip install torch torchvision

# Copy the local directory contents to the container
COPY . .

# Command to run the application
CMD ["python", "main.py"]
