import pandas as pd

class FairnessScoreCalculator:
    def __init__(self, protected_column: str, target_metric: str = "precision"):
        self.protected_column = protected_column
        self.target_metric = target_metric

    def calculate(self, df: pd.DataFrame) -> float:
        group_scores = df.groupby(self.protected_column)[self.target_metric].mean()
        min_score = group_scores.min()
        max_score = group_scores.max()
        if max_score == 0:
            return 0.0
        return round(min_score / max_score, 3)
