from karma_engine.score_calculator import KarmaScoreCalculator

def test_karma_score_basic():
    scorer = KarmaScoreCalculator()
    metrics = {
        "accuracy": 0.90,
        "latency": 1000,
        "drift": 0.05,
        "fairness": 0.88,
        "retrain_days": 10
    }
    score = scorer.calculate_score(metrics)
    assert 0 <= score <= 100
