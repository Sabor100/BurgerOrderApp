# Use the official Python image from the Docker Hub
FROM python:3.9.6-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

EXPOSE 8001

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install the package sqlite3
RUN apt-get update && apt-get install -y sqlite3 libsqlite3-dev

# Define environment variable to tell Flask it's in development mode
ENV FLASK_ENV=development

# Run app.py when the container launches
CMD ["python", "app.py"]
