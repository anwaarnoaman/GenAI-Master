from app.core.celery_app import celery_app
from app.services.document_status import set_status
from app.core.logging import get_logger
from app.services.ingestion_service import ingest_document
logger = get_logger(__name__)

@celery_app.task(bind=True)
def ingest_document_task(self, document_id: str, file_path: str, filename: str):
    try:
        set_status(document_id, "processing")
        logger.info("Processing %s", filename)

        # load → chunk → embed → vector DB
        ingest_document(file_path, filename) 
        set_status(document_id, "completed")
        return {"document_id": document_id, "status": "completed"}

    except Exception as e:
        logger.exception("Failed processing %s", filename)
        set_status(document_id, "failed", str(e))
        raise


 