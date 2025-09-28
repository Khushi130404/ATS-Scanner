from app.model.schema import Resume

def get_resume_skills(resume: Resume) -> list:
    """
    Extract skills from parsed resume object.
    """
    return [s.lower() for s in resume.extracted_data.skills]
