from fastapi import FastAPI
from upload import router

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is running 🚀"}

app.include_router(router)
