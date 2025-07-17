import pandas as pd
import os
from datetime import datetime, timedelta
import random

def simulate_karma_scores(output_path):
    try:
        models = ["XGBoostClassifier", "RandomForestV2", "BERTSentimentModel"]
        start_date = datetime.now() - timedelta(days=30)
        rows = []

        for day in range(30):
            date = start_date + timedelta(days=day)
            for model in models:
                score = round(random.uniform(0.5, 0.98), 2)
                rows.append({
                    "model_name": model,
                    "karma_score": score,
                    "timestamp": date.strftime("%Y-%m-%d %H:%M:%S")
                })

        df = pd.DataFrame(rows)

        # Make sure the folder exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # Save the CSV
        df.to_csv(output_path, index=False)
        print(f"✅ Karma scores saved to: {output_path}")
        print(df.head())  # Show preview of saved data
    except Exception as e:
        print(f"❌ Failed to simulate karma scores: {e}")

if __name__ == "__main__":
    simulate_karma_scores("data/performance_metrics/karma_log.csv")
