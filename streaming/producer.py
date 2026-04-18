import time

def stream(df):
    for _, row in df.iterrows():
        yield row.to_dict()
        time.sleep(0.05)