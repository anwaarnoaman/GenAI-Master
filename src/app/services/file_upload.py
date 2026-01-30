from typing import List
from fastapi import UploadFile
from pathlib import Path
import uuid

from app.tasks.ingest_document import ingest_document_task
from app.services.document_status import set_status
from app.core.logging import get_logger
from app.core.config import settings

logger = get_logger(__name__)
UPLOAD_DIR = Path(settings.temp_file_path)

async def save_multiple_files(files: List[UploadFile]):
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    results = []

    for file in files:
        document_id = str(uuid.uuid4())
        path = UPLOAD_DIR / f"{document_id}_{file.filename}"

        try:
            content = await file.read()
            path.write_bytes(content)

            # 🔹 initial status
            set_status(document_id, "queued")

            #enqueue ONE task per file
            ingest_document_task.delay(
                document_id=document_id,
                file_path=str(path),
                filename=file.filename
            )

            results.append({
                "document_id": document_id,
                "filename": file.filename,
                "status": "queued"
            })

        except Exception as e:
            logger.exception("Upload failed: %s", file.filename)
            set_status(document_id, "failed", str(e))

            results.append({
                "document_id": document_id,
                "filename": file.filename,
                "status": "failed"
            })

    return results
