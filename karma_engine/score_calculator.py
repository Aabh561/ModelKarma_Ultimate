import yaml
import os

class KarmaScoreCalculator:
    def __init__(self, config_path="config/karma_weights.yaml"):
        with open(config_path, "r") as f:
            self.weights = yaml.safe_load(f)

    def normalize(self, value, max_val):
        return 1 - min(value / max_val, 1)

    def calculate_score(self, metrics: dict) -> float:
        # Extract
        acc = metrics.get("accuracy", 0)
        lat = metrics.get("latency", 0)
        drift = metrics.get("drift", 0)
        fair = metrics.get("fairness", 0)
        retrain_days = metrics.get("retrain_days", 0)

        # Normalize
        norm_latency = self.normalize(lat, self.weights["max_latency"])
        norm_drift = self.normalize(drift, self.weights["max_drift"])
        retrain_penalty = min(retrain_days / 30, 1) * self.weights["retrain_penalty_weight"]

        # Weighted Score
        score = (
            acc * self.weights["accuracy_weight"] +
            norm_latency * self.weights["latency_weight"] +
            norm_drift * self.weights["drift_weight"] +
            fair * self.weights["fairness_weight"]
        ) * 100

        # Apply retrain penalty
        final_score = max(score - retrain_penalty * 100, 0)
        return round(final_score, 2)
