class DriftTracker:
    def detect_drift(self, reference_score: float, current_score: float, threshold: float = 0.05) -> bool:
        
        drift = abs(current_score - reference_score)
        return drift > threshold
