class MitigationPlanner:
    def recommend(self, issue_type: str) -> str:
        
        plans = {
            "drift": "Recalibrate data pipelines or retrain model with recent data.",
            "latency": "Optimize model architecture or switch to quantized/ONNX version.",
            "accuracy_drop": "Perform hyperparameter tuning and error analysis.",
            "fairness_issue": "Investigate subgroup bias and consider reweighting or data balancing.",
            "overfitting": "Introduce regularization and check train-test leakage.",
        }
        return plans.get(issue_type, "No known mitigation available for this issue.")
