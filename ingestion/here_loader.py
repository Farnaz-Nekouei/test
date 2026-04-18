import pandas as pd
import os

def load_here(path):
    """
    HERE dataset loader (offline fallback version)
    """

    if not os.path.exists(path):
        raise FileNotFoundError(
            f"[HERE Loader] Missing file: {path}. Run data/bootstrap.py first."
        )

    df = pd.read_csv(path)
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    return df