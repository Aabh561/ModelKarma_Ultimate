import pandas as pd
import xgboost as xgb
import joblib

class MetaKarmaScorer:
    def __init__(self, model_path="data/models/meta_karma_model.pkl"):
        self.model_path = model_path
        self.model = None

    def train(self, df: pd.DataFrame, label_col="karma_score"):
        X = df.drop(columns=[label_col])
        y = df[label_col]
        self.model = xgb.XGBRegressor()
        self.model.fit(X, y)
        joblib.dump(self.model, self.model_path)

    def load(self):
        self.model = joblib.load(self.model_path)

    def predict(self, metrics: dict) -> float:
        if self.model is None:
            raise ValueError("Model not loaded.")
        df = pd.DataFrame([metrics])
        return round(self.model.predict(df)[0], 2)
