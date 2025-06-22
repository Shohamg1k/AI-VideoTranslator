import os
from fastapi import FastAPI, UploadFile, File, Form
from backend.process_video import process_uploaded_video

app = FastAPI()
UPLOADS_DIR = "backend/uploads"

# Ensure upload directory exists
os.makedirs(UPLOADS_DIR, exist_ok=True)

@app.post("/upload/")
async def upload_video(file: UploadFile = File(...), target_language: str = Form(...)):
    """Handles video upload and starts processing."""
    file_path = os.path.join(UPLOADS_DIR, file.filename)
    
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())
    
    process_uploaded_video(file_path, target_language)

    return {"message": "Processing started", "file": file.filename, "target_language": target_language}
