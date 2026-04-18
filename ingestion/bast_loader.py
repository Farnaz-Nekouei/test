import pandas as pd
import os

def load_bast(path):
    """
    BASt traffic loader with safe fallback handling
    """

    if not os.path.exists(path):
        raise FileNotFoundError(
            f"[BASt Loader] Missing file: {path}. Run data/bootstrap.py first."
        )

    df = pd.read_csv(path)
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    return df