# backend/utils.py
import os
import pandas as pd

BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, "data")

def load_csv(filename, parse_dates=None):
    """Load CSV from backend/data with optional date parsing."""
    path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    df = pd.read_csv(path)
    if parse_dates:
        for col in parse_dates:
            df[col] = pd.to_datetime(df[col])
    return df
