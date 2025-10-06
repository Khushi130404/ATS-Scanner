from fastapi import APIRouter
from app.model.schema import ResumeJobRequest
from app.services.ats_scoring import score_resume
from app.services.job_based_suggestions import ai_suggestions

router = APIRouter()

@router.post("/score")
def ats_score(request: ResumeJobRequest):
    """
    Endpoint to score a resume against a job description.
    """
    return ai_suggestions(request.dict());
    # return ai_suggestions(score_resume(request.resume, request.job_description))
