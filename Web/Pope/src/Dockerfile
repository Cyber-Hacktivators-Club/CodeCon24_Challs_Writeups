# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app
COPY docker-entrypoint.sh /docker-entrypoint.sh

# Install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends netcat-openbsd curl socat && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN chmod +x /docker-entrypoint.sh

# Expose the port that Flask runs on
EXPOSE 8080

# Define environment variable for Flask
ENV FLASK_APP=File.py

CMD ["python File.py"]
