import random

class ShadowScoreSimulator:
    def simulate(self, base_score: float, noise_level: float = 5.0) -> float:
        
        noise = random.uniform(-noise_level, noise_level)
        return round(max(0, min(100, base_score + noise)), 2)
