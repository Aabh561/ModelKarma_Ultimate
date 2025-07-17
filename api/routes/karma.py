from fastapi import APIRouter, HTTPException
from karma_engine.score_calculator import KarmaScoreCalculator
from llm_commentator.karma_commentary_generator import KarmaCommentaryGenerator

router = APIRouter()
scorer = KarmaScoreCalculator()
commentator = KarmaCommentaryGenerator()

@router.post("/karma")
def get_karma_score(metrics: dict):
    try:
        score = scorer.calculate_score(metrics)
        comment = commentator.generate(metrics, score)
        return {"karma_score": score, "commentary": comment}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
