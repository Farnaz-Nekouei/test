import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def generate_plots(df):
    """
    Generates all figures required for LaTeX paper.
    """

    print("Generating figures...")

    os.makedirs("reports/figures", exist_ok=True)

    df = df.copy()

    # Ensure timestamp exists
    if "timestamp" in df:
        df = df.sort_values("timestamp")

    # -----------------------------
    # 1. TIME SERIES
    # -----------------------------
    plt.figure()
    if "timestamp" in df and "vehicles" in df:
        plt.plot(df["timestamp"], df["vehicles"])
        plt.xlabel("Time")
        plt.ylabel("Flow (veh/h)")
        plt.title("Traffic Flow Time Series")
        plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("reports/figures/time_series_decomposition.png")
    plt.close()

    # -----------------------------
    # 2. CORRELATION MATRIX
    # -----------------------------
    plt.figure()
    numeric_df = df.select_dtypes(include=[np.number])

    if len(numeric_df.columns) > 1:
        corr = numeric_df.corr()
        plt.imshow(corr)
        plt.colorbar()
        plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
        plt.yticks(range(len(corr.columns)), corr.columns)
        plt.title("Correlation Matrix")

    plt.tight_layout()
    plt.savefig("reports/figures/correlation_matrix.png")
    plt.close()

    # -----------------------------
    # 3. PHASE SPACE
    # -----------------------------
    plt.figure()
    if "vehicles" in df and "speed" in df:
        plt.scatter(df["vehicles"], df["speed"], alpha=0.5)
        plt.xlabel("Flow (veh/h)")
        plt.ylabel("Speed (km/h)")
        plt.title("Phase Space")
    plt.tight_layout()
    plt.savefig("reports/figures/phase_space.png")
    plt.close()

    # -----------------------------
    # 4. 3D SURFACE
    # -----------------------------
    from mpl_toolkits.mplot3d import Axes3D  # noqa

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    if "vehicles" in df and "speed" in df:
        x = np.arange(len(df))
        y = df["vehicles"].fillna(0).values
        z = df["speed"].fillna(0).values

        ax.scatter(x, y, z)
        ax.set_xlabel("Time Index")
        ax.set_ylabel("Flow")
        ax.set_zlabel("Speed")

    plt.tight_layout()
    plt.savefig("reports/figures/3d_surface.png")
    plt.close()

    # -----------------------------
    # 5. SHOCKWAVE (SAFE)
    # -----------------------------
    plt.figure()

    if "vehicles" in df:
        series = df["vehicles"].dropna()

        if len(series) > 2:
            grad = np.gradient(series)
            plt.plot(grad)
            plt.title("Shockwave Approximation (Flow Gradient)")
            plt.xlabel("Time Index")
            plt.ylabel("dFlow/dt")
        else:
            plt.text(0.5, 0.5, "Not enough data",
                     ha="center", va="center")
            plt.title("Shockwave Approximation (Insufficient Data)")

    plt.tight_layout()
    plt.savefig("reports/figures/shockwave.png")
    plt.close()

    print("✅ Figures saved to reports/figures/")