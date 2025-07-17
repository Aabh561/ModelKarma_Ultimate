def explain_rule(karma_score):
    if karma_score > 0.9:
        return "Model is performing excellently under current rules."
    elif karma_score > 0.75:
        return "Model is stable, but minor calibration is advised."
    else:
        return "Model needs intervention based on drift or metric drop."
