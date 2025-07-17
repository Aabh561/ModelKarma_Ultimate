class PerformanceWatcher:
    def check_thresholds(self, metrics: dict, thresholds: dict) -> dict:
        
        failures = {}
        for key, value in metrics.items():
            if key in thresholds and value < thresholds[key]:
                failures[key] = f"{value} < {thresholds[key]}"
        return failures
