from fastapi import APIRouter, UploadFile, File
import os

router = APIRouter()

UPLOAD_PATH = "data/uploaded.csv"

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    os.makedirs("data", exist_ok=True)

    with open(UPLOAD_PATH, "wb") as f:
        f.write(await file.read())

    return {"message": "File uploaded successfully"}
