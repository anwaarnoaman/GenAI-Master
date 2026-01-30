FROM python:3.12-slim

WORKDIR /app
COPY pyproject.toml .
RUN pip install --no-cache-dir -U pip && pip install .

COPY src ./src
CMD ["celery", "-A", "app.core.celery_app.celery_app", "worker", "--loglevel=info"]
