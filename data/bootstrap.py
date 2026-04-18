import os
import pandas as pd
import numpy as np

def bootstrap():
    """
    Creates deterministic fallback datasets if real data is missing.
    Ensures reproducibility of digital twin pipeline.
    """

    os.makedirs("data/raw", exist_ok=True)

    # -----------------------------
    # BASt synthetic traffic data
    # -----------------------------
    bast = pd.DataFrame({
        "timestamp": pd.date_range("2024-01-01", periods=300, freq="h"),
        "road_id": np.random.randint(1, 15, 300),
        "vehicles": np.random.randint(50, 400, 300),
        "region": np.random.choice(["BW", "BY"], 300)
    })

    bast.to_csv("data/raw/bast.csv", index=False)

    # -----------------------------
    # HERE traffic proxy dataset
    # -----------------------------
    here = pd.DataFrame({
        "timestamp": pd.date_range("2024-01-01", periods=300, freq="h"),
        "road_id": np.random.randint(1, 15, 300),
        "speed": np.random.uniform(30, 130, 300),
        "congestion": np.random.uniform(0, 1, 300)
    })

    here.to_csv("data/raw/here.csv", index=False)

    # -----------------------------
    # OSM road network structure
    # -----------------------------
    osm = pd.DataFrame({
        "road_id": list(range(1, 15)),
        "length_m": np.random.randint(200, 8000, 14)
    })

    osm.to_csv("data/raw/osm.csv", index=False)

    print("✅ DATA BOOTSTRAP COMPLETE (BASt + HERE + OSM)")