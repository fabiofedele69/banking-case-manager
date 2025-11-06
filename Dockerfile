FROM python:3.11-slim

# Install OS-level deps required for psycopg2
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements first for better cache behavior
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENV PORT=8080
EXPOSE 8080

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8080", "--workers", "1"]
