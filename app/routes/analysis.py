from fastapi import APIRouter
import pandas as pd
import os

router = APIRouter()

FILE_PATH = "data/uploaded.csv"

@router.get("/analysis")
def get_analysis():
    if not os.path.exists(FILE_PATH):
        return {"error": "No file uploaded yet"}

    df = pd.read_csv(FILE_PATH)

    summary = df.describe().to_dict()
    correlation = df.corr(numeric_only=True).to_dict()

    return {
        "summary": summary,
        "correlation": correlation
    }