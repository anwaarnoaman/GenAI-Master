from fastapi import FastAPI
from app.core.logging import setup_logging, get_logger
from app.core.config import settings
from app.api.health import router as health_router

setup_logging()
logger = get_logger(__name__)

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    version="0.1.0",
)

app.include_router(health_router)


@app.get("/")
def root():
    logger.info("Root endpoint called")
    return {"status": "ok"}
