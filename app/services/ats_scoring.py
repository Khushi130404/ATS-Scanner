from app.services.llm_skill_extractor import extract_skills_from_jd
from app.utils.resume_utils import get_resume_skills

def score_resume(resume_json: dict, job_description: str) -> dict:
    """
    Score resume based on matched skills from JD.
    """
    resume_skills = get_resume_skills(resume_json)

    required_skills = [s.lower() for s in extract_skills_from_jd(job_description)]

    matched_skills = list(set(resume_skills) & set(required_skills))

    score = round((len(matched_skills) / len(required_skills)) * 100, 2) if required_skills else 0

    return {
        "score": score,
        "matched_skills": matched_skills,
        "required_skills": required_skills,
        "total_required_skills": len(required_skills)
    }
