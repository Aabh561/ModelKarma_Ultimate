import pandas as pd
from datetime import datetime

def init_karma_scores(output_path: str):
    
    df = pd.DataFrame(columns=["model_name", "karma_score", "timestamp"])
    df.to_csv(output_path, index=False)
