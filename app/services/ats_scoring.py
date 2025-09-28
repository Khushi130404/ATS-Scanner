from app.utils import resume_utils
from app.services import llm_skill_extractor

def score_resume(parsed_resume: dict, job_description: str) -> dict:
    """
    Score the resume against the job description.
    """
    resume_skills = resume_utils.get_resume_skills(parsed_resume)
    jd_skills = llm_skill_extractor.extract_skills_from_jd(job_description)

    matched_skills = [skill for skill in resume_skills if skill in jd_skills]
    missing_skills = [skill for skill in jd_skills if skill not in resume_skills]

    score = int((len(matched_skills) / len(jd_skills)) * 100) if jd_skills else 0

    return {
        "score": score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "total_resume_skills": len(resume_skills),
        "total_jd_skills": len(jd_skills)
    }
