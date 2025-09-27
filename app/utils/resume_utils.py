def get_resume_skills(parsed_resume: dict) -> list:
    """
    Extract skills from parsed resume JSON.
    """
    skills = parsed_resume.get("extracted_data", {}).get("skills", [])
    return [s.lower() for s in skills]
