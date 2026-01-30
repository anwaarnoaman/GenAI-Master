# ==============================
# Base image (Python 3.12)
# ==============================
FROM python:3.12-slim

# ==============================
# Environment variables
# ==============================
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ==============================
# Working directory
# ==============================
WORKDIR /app

# ==============================
# System dependencies (optional but safe)
# ==============================
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# ==============================
# Install Python dependencies
# ==============================
COPY pyproject.toml .
RUN pip install --upgrade pip \
    && pip install .

# ==============================
# Copy application source
# ==============================
COPY src ./src
COPY .env .env

# ==============================
# Expose FastAPI port
# ==============================
EXPOSE 8000

# ==============================
# Run FastAPI
# ==============================
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
 