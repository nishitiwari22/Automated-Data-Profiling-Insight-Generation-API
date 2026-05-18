from fastapi import APIRouter
from fastapi.responses import Response
import pandas as pd
import matplotlib.pyplot as plt
import io
import os

router = APIRouter()

FILE_PATH = "data/uploaded.csv"

@router.get("/visualization")
def get_visualization():
    if not os.path.exists(FILE_PATH):
        return {"error": "No file uploaded"}

    df = pd.read_csv(FILE_PATH)

    # Create simple plot
    plt.figure()
    df.select_dtypes(include='number').hist(figsize=(8, 6))

    # Save to buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()

    return Response(content=buf.getvalue(), media_type="image/png")