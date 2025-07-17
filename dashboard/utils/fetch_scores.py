import pandas as pd

def fetch_latest_scores():
    return pd.read_csv("data/performance_metrics/karma_log.csv")
