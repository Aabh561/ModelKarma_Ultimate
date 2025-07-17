import pandas as pd
from dowhy import CausalModel

class CausalExplainer:
    def __init__(self, data: pd.DataFrame, treatment: str, outcome: str):
        self.model = CausalModel(
            data=data,
            treatment=treatment,
            outcome=outcome,
            common_causes=data.columns.drop([treatment, outcome]).tolist()
        )

    def identify(self):
        return self.model.identify_effect()

    def estimate(self, method_name="backdoor.propensity_score_matching"):
        identified_estimand = self.identify()
        return self.model.estimate_effect(identified_estimand, method_name=method_name)

    def refute(self, estimate, method_name="placebo_treatment_refuter"):
        return self.model.refute_estimate(estimate, method_name=method_name)
