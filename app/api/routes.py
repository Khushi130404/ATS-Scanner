from fastapi import APIRouter
from app.models.schema import ResumeJobRequest
from app.services.ats_scoring import score_resume

router = APIRouter()

@router.post("/score")
def ats_score(request: ResumeJobRequest):
    """
    Endpoint to score a resume against a job description.
    """
    result = score_resume(request.resume, request.job_description)
    return result
