from app.core.logging import get_logger
# from app.services.vector_store import store_embeddings

logger = get_logger(__name__)

def ingest_document(file_path: str, filename: str):
    logger.info("Processing %s", filename)

    # 1. Load document
    # 2. Chunk
    # 3. Embed
    # 4. Store in vector DB

    # store_embeddings(file_path)