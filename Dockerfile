# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Expose the port the app runs on (Gradio default)
EXPOSE 7860

# Define environment variable for Gradio (optional)
ENV GRADIO_SERVER_PORT=7860

# Run the application
CMD ["python", "main.py"]
