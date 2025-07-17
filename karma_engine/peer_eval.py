class PeerEvaluator:
    def __init__(self, agreement_threshold=0.85):
        self.agreement_threshold = agreement_threshold

    def calculate_agreement(self, outputs: list[str]) -> float:
        if not outputs:
            return 0.0
        most_common = max(set(outputs), key=outputs.count)
        count = outputs.count(most_common)
        return round(count / len(outputs), 3)

    def score_model(self, model_output: str, peer_outputs: list[str]) -> float:
        agreement = peer_outputs.count(model_output) / len(peer_outputs)
        return round(agreement, 3)
