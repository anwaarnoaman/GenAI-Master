from fastapi import APIRouter
from app.core.logging import get_logger

logger = get_logger(__name__)

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("")
def health_check():
    logger.info("OK")
    return {"status": "ok"}
