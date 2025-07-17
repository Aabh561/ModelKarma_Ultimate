from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime

class FairnessReportGenerator:
    def __init__(self, save_path="data/performance_metrics/fairness_report.pdf"):
        self.save_path = save_path

    def generate(self, model_name: str, metrics: dict, subgroup_scores: dict):
        c = canvas.Canvas(self.save_path, pagesize=A4)
        width, height = A4

        c.setFont("Helvetica-Bold", 18)
        c.drawString(50, height - 50, f"Fairness Audit Report - {model_name}")

        c.setFont("Helvetica", 12)
        c.drawString(50, height - 80, f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        c.drawString(50, height - 120, "Overall Fairness Metrics:")
        y = height - 140
        for k, v in metrics.items():
            c.drawString(60, y, f"{k}: {v}")
            y -= 20

        c.drawString(50, y - 20, "Subgroup Scores:")
        y -= 40
        for subgroup, score in subgroup_scores.items():
            c.drawString(60, y, f"{subgroup}: {score}")
            y -= 20

        c.save()
