import pandas as pd
import numpy as np

def clean(df):
    """
    Robust cleaning for heterogeneous traffic digital twin data
    """

    df = df.copy()

    # ----------------------------
    # Keep only numeric columns
    # ----------------------------
    numeric_df = df.select_dtypes(include=[np.number])

    # ----------------------------
    # Handle missing values safely
    # ----------------------------
    numeric_df = numeric_df.fillna(numeric_df.mean())

    # ----------------------------
    # Z-score normalization (safe)
    # ----------------------------
    z = (numeric_df - numeric_df.mean()) / (numeric_df.std() + 1e-9)

    # ----------------------------
    # Merge back categorical cols
    # ----------------------------
    categorical_df = df.select_dtypes(exclude=[np.number])

    cleaned = pd.concat([categorical_df.reset_index(drop=True),
                         z.reset_index(drop=True)], axis=1)

    return cleaned