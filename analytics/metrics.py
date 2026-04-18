import pandas as pd
import numpy as np

def compute_metrics(df):
    """
    Computes aggregated traffic metrics for BW and BY regions.
    Safe for missing columns and mixed data.
    """

    df = df.copy()

    # Ensure required columns exist
    for col in ["speed", "vehicles", "congestion"]:
        if col not in df:
            df[col] = 0.0

    # Split by region
    if "region" in df:
        bw = df[df["region"] == "BW"]
        by = df[df["region"] == "BY"]
    else:
        bw = df
        by = df

    # Safe mean helper
    def safe_mean(series):
        return float(series.mean()) if len(series) > 0 else 0.0

    metrics = {
        "bw": {
            "speed_mean": safe_mean(bw["speed"]),
            "flow_mean": safe_mean(bw["vehicles"]),
            "congestion_mean": safe_mean(bw["congestion"]),
        },
        "by": {
            "speed_mean": safe_mean(by["speed"]),
            "flow_mean": safe_mean(by["vehicles"]),
            "congestion_mean": safe_mean(by["congestion"]),
        },
        "corr": {
            # placeholders until real correlation layer added
            "weather_congestion": float(np.corrcoef(df["speed"], df["congestion"])[0,1]) if len(df) > 1 else 0.0,
            "economic_traffic": float(np.corrcoef(df["vehicles"], df["speed"])[0,1]) if len(df) > 1 else 0.0,
            "speed_density": float(np.corrcoef(df["speed"], df["vehicles"])[0,1]) if len(df) > 1 else 0.0,
        }
    }

    return metrics