from fastapi import FastAPI
from app.routes import upload, analysis, visualization

app = FastAPI(title="Data Insights API")

# Include all routers
app.include_router(upload.router)
app.include_router(analysis.router)
app.include_router(visualization.router)


# Optional: Root endpoint (health check)
@app.get("/")
def root():
    return {"message": "Data Insights API is running 🚀"}