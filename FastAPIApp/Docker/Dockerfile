# Use Python 3.12 slim as the base image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY ../FastAPIApp/FastAPIChaos/requirements.txt .

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI application code into the container
COPY ../FastAPIApp/FastAPIChaos /app

# Expose the port that FastAPI will run on
EXPOSE 8080

# Command to run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
