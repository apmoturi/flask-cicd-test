FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PORT=3333
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY app/ .

# Expose port
EXPOSE ${PORT}

# Use gunicorn for better production performance
CMD ["gunicorn", "--bind", "0.0.0.0:3333", "--workers", "3", "app:app"]
