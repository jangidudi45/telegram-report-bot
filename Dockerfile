# Base image (Python 3.11)
FROM python:3.11-slim

# Working directory inside container
WORKDIR /app

# Install dependencies from requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Install Flask for health check endpoint
RUN pip install flask

# Run health.py in background and then start bot.py
CMD ["sh", "-c", "python health.py & python bot.py"]
