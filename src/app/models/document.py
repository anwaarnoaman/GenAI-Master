from pydantic import BaseModel
from typing import List

class UploadedDocument(BaseModel):
    document_id: str
    filename: str
    status: str

class MultiUploadResponse(BaseModel):
    total: int
    uploaded: List[UploadedDocument]
