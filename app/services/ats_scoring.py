from app.utils import resume_utils
from app.services.llm_skill_extractor import extract_skills_from_jd
from app.services.skills_mapping import map_domain_skills

def score_resume(parsed_resume: dict, job_description: str) -> dict:
    """
    Score the resume against the job description.
    """
    # Get skills from resume
    resume_skills = resume_utils.get_resume_skills(parsed_resume)

    # Get skills from job description using LLM
    jd_skills = extract_skills_from_jd(job_description)

    # Add domain skills automatically
    jd_skills = map_domain_skills(job_description, jd_skills)

    # Lowercase everything for matching
    resume_skills = [s.lower() for s in resume_skills]
    jd_skills = [s.lower() for s in jd_skills]

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