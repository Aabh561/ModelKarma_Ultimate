
import numpy as np
from typing import List, Tuple

class AutoRetrainSuggester:
    def __init__(self, decay_threshold=0.15, max_retrain_gap=30, volatility_threshold=0.1):
        self.decay_threshold = decay_threshold
        self.max_retrain_gap = max_retrain_gap
        self.volatility_threshold = volatility_threshold

    def _calculate_trend_slope(self, scores: List[float]) -> float:
        if len(scores) < 3:
            return 0.0
        x = np.arange(len(scores))
        y = np.array(scores)
        slope = np.polyfit(x, y, 1)[0]
        return slope

    def _calculate_volatility(self, scores: List[float]) -> float:
        if len(scores) < 2:
            return 0.0
        return np.std(scores)

    def should_retrain(self, scores: List[float], days_since_retrain: int) -> Tuple[bool, str]:
        if len(scores) < 2:
            return False, "🟢 Not enough data to assess retraining."

        decay = scores[-2] - scores[-1]
        slope = self._calculate_trend_slope(scores)
        volatility = self._calculate_volatility(scores)

        if decay >= self.decay_threshold:
            return True, f"⚠️ Retrain suggested: sudden karma drop of {decay:.2f}"

        if slope < -0.01:
            return True, f"⚠️ Retrain suggested: negative trend detected (slope {slope:.3f})"

        if volatility > self.volatility_threshold:
            return True, f"⚠️ Retrain suggested: high score volatility ({volatility:.2f})"

        if days_since_retrain > self.max_retrain_gap:
            return True, f"⏳ Retrain suggested: last retrain was {days_since_retrain} days ago"

        return False, "✅ Model is stable. No retraining needed now."
