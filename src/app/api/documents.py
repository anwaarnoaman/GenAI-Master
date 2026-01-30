from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import List

from app.services.file_upload import save_multiple_files
from app.models.document import MultiUploadResponse
from app.core.logging import get_logger
from app.services.document_status import get_status


router = APIRouter(prefix="/documents", tags=["Documents"])
logger = get_logger(__name__)

@router.post("/upload", response_model=MultiUploadResponse)
async def upload_documents(
    files: List[UploadFile] = File(...)
):
    if not files:
        raise HTTPException(status_code=400, detail="No files uploaded")

    logger.info("Received %d files for upload", len(files))

    try:
        results = await save_multiple_files(files)
        return MultiUploadResponse(
            total=len(files),
            uploaded=results,
        )
    except Exception:
        logger.exception("Multiple file upload failed")
        raise HTTPException(status_code=500, detail="Upload failed")



@router.get("/{document_id}/status")
def document_status(document_id: str):
    status = get_status(document_id)
    if not status:
        raise HTTPException(status_code=404, detail="Document not found")
    return status