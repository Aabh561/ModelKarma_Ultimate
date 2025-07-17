class KarmaNormalizer:
    def normalize(self, raw_score: float) -> float:
       
        return round(max(0.0, min(100.0, raw_score)), 2)
