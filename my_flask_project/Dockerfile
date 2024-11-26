# Use the official Python image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY ./app ./app

# Expose the Flask app's port
EXPOSE 5000

# Start Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
