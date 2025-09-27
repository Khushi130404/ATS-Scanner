from app.services.llm_skill_extractor import extract_skills_from_jd

def score_resume(resume: dict, job_description: str) -> dict:
    resume_skills = [s.lower() for s in resume.get("skills", [])]

    # LLM extracts required skills from JD
    required_skills = [s.lower() for s in extract_skills_from_jd(job_description)]

    # Matching
    matched_skills = list(set(resume_skills) & set(required_skills))
    score = round((len(matched_skills) / len(required_skills)) * 100, 2) if required_skills else 0

    return {
        "score": score,
        "matched_skills": matched_skills,
        "required_skills": required_skills,
        "total_required_skills": len(required_skills)
    }
