# Use a small Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Install dependencies first (so Docker can cache this layer)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Flask runs on port 5000
EXPOSE 5000

CMD ["python", "app.py"]