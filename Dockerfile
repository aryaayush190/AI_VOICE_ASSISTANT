# Use an official Python runtime as a parent image.
FROM python:3.9-slim

# Set environment variables to prevent Python from writing .pyc files
# and to ensure output is sent straight to the terminal (unbuffered).
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container to /app.
WORKDIR /app

# Copy the requirements file into the container at /app.
COPY requirements.txt .

# Upgrade pip and install the required dependencies.
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application code to /app.
COPY . .

# Expose port 8000 so the container can be accessed externally.
EXPOSE 8000

# Define the command to run your application using uvicorn.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
