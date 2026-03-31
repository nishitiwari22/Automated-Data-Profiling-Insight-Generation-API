from fastapi import FastAPI
from app.routes import upload, analysis

app = FastAPI()

app.include_router(upload.router)
app.include_router(analysis.router)

