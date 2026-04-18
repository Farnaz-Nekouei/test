import os

from data.bootstrap import bootstrap

from ingestion.bast_loader import load_bast
from ingestion.here_loader import load_here
from ingestion.osm_loader import load_osm

from processing.cleaning import clean
from processing.fusion import fuse

from analytics.metrics import compute_metrics
from analytics.export_latex import inject_tables

from visualization.plots import generate_plots


def run_bw_by():
    print("\n================ BW/BY DIGITAL TWIN ================\n")

    # --------------------------------------------------
    # 1. ENSURE DATA EXISTS
    # --------------------------------------------------
    bootstrap()

    # --------------------------------------------------
    # 2. LOAD DATA
    # --------------------------------------------------
    bast = load_bast("data/raw/bast.csv")
    here = load_here("data/raw/here.csv")
    osm = load_osm("data/raw/osm.csv")

    # --------------------------------------------------
    # 3. CLEANING
    # --------------------------------------------------
    bast = clean(bast)
    here = clean(here)

    # --------------------------------------------------
    # 4. FUSION (DIGITAL TWIN CORE)
    # --------------------------------------------------
    df = fuse(bast, here, osm)

    # --------------------------------------------------
    # 5. ANALYTICS
    # --------------------------------------------------
    metrics = compute_metrics(df)

    # --------------------------------------------------
    # 6. VISUALIZATION
    # --------------------------------------------------
    generate_plots(df)

    # --------------------------------------------------
    # 7. LATEX EXPORT
    # --------------------------------------------------
    inject_tables(metrics)

    print("\n✅ BW/BY DIGITAL TWIN PIPELINE COMPLETE\n")



if __name__ == "__main__":
    print("\n🚀 STARTING FULL DIGITAL TWIN PIPELINE\n")

    run_bw_by()

    print("\n🎯 ALL SYSTEMS COMPLETE\n")