from fastapi import APIRouter, UploadFile, File, HTTPException
import fitz

from app.services.chunking_service import (
    fixed_size_chunking,
    sentence_chunking
)


router = APIRouter(prefix="/documents", tags=["Documents"])


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
    chunking_strategy: str = "fixed"
):
    if file.content_type not in ["application/pdf", "text/plain"]:
        raise HTTPException(
            status_code=400,
            detail="Only PDF and TXT files are supported."
        )

    if chunking_strategy not in ["fixed", "sentence"]:
        raise HTTPException(
            status_code=400,
            detail="Chunking strategy must be 'fixed' or 'sentence'."
        )

    file_content = await file.read()

    # Extract text
    if file.content_type == "application/pdf":
        document = fitz.open(
            stream=file_content,
            filetype="pdf"
        )

        text = ""

        for page in document:
            text += page.get_text()

        document.close()

    else:
        text = file_content.decode("utf-8")

    # Apply selected chunking strategy
    if chunking_strategy == "fixed":
        chunks = fixed_size_chunking(text)

    else:
        chunks = sentence_chunking(text)

    return {
        "filename": file.filename,
        "file_type": file.content_type,
        "chunking_strategy": chunking_strategy,
        "total_chunks": len(chunks),
        "chunks": chunks
    }