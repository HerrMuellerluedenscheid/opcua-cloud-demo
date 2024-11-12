# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY server/. .

# Expose the port that the server will run on
EXPOSE 4840/tcp

# Command to run the server
CMD ["python", "main.py"]
