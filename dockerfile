FROM python:3.9

# Set working directory
WORKDIR /app

# Copy the application files
COPY app.py .
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the application
CMD ["python", "app.py"]
