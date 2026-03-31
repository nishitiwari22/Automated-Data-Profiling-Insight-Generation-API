from fastapi import APIRouter
import pandas as pd
from fastapi.responses import FileResponse

from app.services.data_cleaning import clean_data
from app.services.analysis_service import get_summary, get_correlation, get_basic_insights
from app.services.visualization_service import generate_correlation_heatmap

router = APIRouter()

DATA_PATH = "data/uploaded.csv"

@router.get("/summary")
def summary():
    df = pd.read_csv(DATA_PATH)
    df = clean_data(df)
    return get_summary(df)

@router.get("/correlation")
def correlation():
    df = pd.read_csv(DATA_PATH)
    df = clean_data(df)
    return get_correlation(df)

# 🔥 NEW
@router.get("/insights")
def insights():
    df = pd.read_csv(DATA_PATH)
    df = clean_data(df)
    return get_basic_insights(df)

# 🔥 NEW
@router.get("/heatmap")
def heatmap():
    df = pd.read_csv(DATA_PATH)
    df = clean_data(df)
    path = generate_correlation_heatmap(df)
    return FileResponse(path)