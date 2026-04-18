import pandas as pd

def fuse(bast, here, osm):
    """
    Digital twin data fusion layer:
    combines BASt + HERE + OSM into unified traffic state
    """

    # ensure consistent keys exist
    bast = bast.copy()
    here = here.copy()
    osm = osm.copy()

    # standardize column names safely
    for df in [bast, here, osm]:
        if "road_id" not in df.columns:
            df["road_id"] = 0
        if "timestamp" not in df.columns:
            df["timestamp"] = pd.Timestamp.utcnow()

        # Ensure consistent key types
    bast["road_id"] = bast["road_id"].astype(str)
    here["road_id"] = here["road_id"].astype(str)
    osm["road_id"] = osm["road_id"].astype(str)
    
    # merge core streams
    df = bast.merge(here, on=["road_id", "timestamp"], how="outer")

    # OSM enrich (spatial structure)
    if "length_km" in osm.columns:
        df = df.merge(osm[["road_id", "length_km"]], on="road_id", how="left")
    else:
        df["length_km"] = 1.0

    # engineered features (DIGITAL TWIN STATE)
    df["flow"] = df.get("vehicles", 0)
    df["density"] = df["flow"] / df["length_km"]
    df["speed_index"] = df.get("speed", 0) / (df["density"] + 1e-6)

    return df