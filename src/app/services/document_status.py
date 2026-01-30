import redis
from app.core.config import settings

redis_client = redis.Redis.from_url(
    settings.redis_url,
    decode_responses=True
)

def set_status(doc_id: str, status: str, error: str | None = None):
    data = {"status": status}
    if error:
        data["error"] = error
    redis_client.hset(f"document:{doc_id}", mapping=data)

def get_status(doc_id: str) -> dict:
    return redis_client.hgetall(f"document:{doc_id}")
