import pandas as pd
from prophet import Prophet

class KarmaTrendForecaster:
    def __init__(self):
        self.model = Prophet()

    def fit(self, df: pd.DataFrame):
        self.model.fit(df)

    def predict(self, periods: int = 7) -> pd.DataFrame:
        future = self.model.make_future_dataframe(periods=periods)
        forecast = self.model.predict(future)
        return forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]]
