from llm_commentator.karma_commentary_generator import KarmaCommentaryGenerator

def test_commentary_generation():
    commentator = KarmaCommentaryGenerator()
    metrics = {
        "accuracy": 0.75,
        "latency": 1800,
        "drift": 0.15,
        "fairness": 0.82,
        "retrain_days": 40
    }
    comment = commentator.generate(metrics, score=62.0)
    assert "Karma score of" in comment
