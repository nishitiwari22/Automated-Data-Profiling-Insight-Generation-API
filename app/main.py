from fastapi import FastAPI
<<<<<<< HEAD
from app.routes import upload, analysis, visualization
=======
from upload import router
>>>>>>> 7bc52a3fc8f241ec1686823621d30c67496576dd

app = FastAPI(title="Data Insights API")

<<<<<<< HEAD
# Include all routers
app.include_router(upload.router)
app.include_router(analysis.router)
app.include_router(visualization.router)


# Optional: Root endpoint (health check)
@app.get("/")
def root():
    return {"message": "Data Insights API is running 🚀"}
=======
@app.get("/")
def home():
    return {"message": "API is running 🚀"}

app.include_router(router)
>>>>>>> 7bc52a3fc8f241ec1686823621d30c67496576dd
