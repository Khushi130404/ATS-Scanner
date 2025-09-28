from app.constants.domain_skills import *

def map_domain_skills(job_description: str, extracted_skills: list) -> list:
    jd_lower = job_description.lower()
    domain_mapping = {
        "big data": BIG_DATA_SKILLS,
        "cybersecurity": CYBERSECURITY_SKILLS,
        "data science": DATA_SCIENCE_SKILLS,
        "web development": WEB_DEV_SKILLS,
        "cloud": CLOUD_COMPUTING_SKILLS,
        "mobile": MOBILE_DEV_SKILLS
    }
    
    for keyword, skills in domain_mapping.items():
        if keyword in jd_lower:
            extracted_skills += skills
    
    return list(set([s.lower() for s in extracted_skills]))
