import pandas as pd
import os

def load_osm(path):

    if not os.path.exists(path):
        raise FileNotFoundError(
            f"[OSM Loader] Missing file: {path}. Run data/bootstrap.py first."
        )

    df = pd.read_csv(path)

    df["length_km"] = df["length_m"] / 1000

    return df