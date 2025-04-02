# Use Python 3.12 slim as the base image
FROM python:3.13-slim

# Set the working directory inside the container
WORKDIR /app
COPY . /app
#copying entire .venv
# COPY .venv /app/.venv


# Copy the rest of your application files
# COPY . /app
# Copy requirements.txt to the working directory in the container
# COPY requirements.txt .

# Copy requirements and local packages into the container
COPY requirements.txt .
COPY local_packages /app/local_packages

# ENV http_proxy http://127.0.0.1:3128
# ENV https_proxy http://127.0.0.1:3128

# Install the Python dependencies using the local packages
RUN pip install --no-index --find-links=/app/local_packages -r requirements.txt

# Install dependencies from requirements.txt
#Run PIP upgrade
# RUN pip install --upgrade pip
# RUN apk add --no-cache ca-certificates && update-ca-certificates && \
    # pip install --upgrade pip --trusted-host pypi.org --trusted-host files.pythonhosted.org

    # Copy the rest of your application code
# COPY . .

# RUN pip install --no-cache-dir -r requirements.txt

# RUN pip install --no-cache-dir -r requirements.txt

#Install from local
# RUN pip install --no-index --find-links=/app/.venv/Lib/site-packages -r requirements.txt
# Install packages using the local .venv environment
# RUN pip install --no-index --find-links=/app/.venv/Lib/site-packages -r requirements.txt
# Copy the rest of the application code to the working directory in the container

###
# Set the working directory in the container
# WORKDIR /app

# Copy the requirements.txt file into the container
# COPY requirements.txt /app/requirements.txt

# Install the packages using requirements.txt
# RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . .

# Expose port 8080
EXPOSE 8010

# Run the FastAPI app with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8010"]
