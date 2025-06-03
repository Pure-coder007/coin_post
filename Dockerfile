FROM python:3.9-slim

WORKDIR /app

# Install system dependencies for psycopg2 and other potential requirements
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Alternative if you want to use psycopg2-binary instead:
# RUN pip install --no-cache-dir psycopg2-binary==2.9.3

# Copy application code
COPY . .

# Expose port 8000
EXPOSE 8000

# Command to run the application with gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8000", "-w", "4", "runserver:app"]

