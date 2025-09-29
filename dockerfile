# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy app code
COPY . .

EXPOSE 8080

# Use gunicorn for a production-ready server
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "server:app"]
