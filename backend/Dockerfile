# Use a base image with Python
FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV APP_HOME /app

# Set the working directory
WORKDIR $APP_HOME

# Install system dependencies
RUN apt-get update && \
    apt-get install -y postgresql-client && \
    rm -rf /var/lib/apt/lists/*

# Copy dependencies file
COPY requirements.txt .

# Install Python dependencies, specifying pg_config path
RUN apt-get update && \
    apt-get install -y build-essential libpq-dev && \
    rm -rf

# Copy the project files to the container
COPY . .

# Expose the FastAPI server port
EXPOSE 8000

# Command to run when starting the container
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
