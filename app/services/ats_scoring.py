from app.utils import resume_utils
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

MODEL_NAME = "google/flan-t5-base"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

def extract_skills_from_jd(job_description: str) -> list:
    """
    Given a job description, return a list of required skills using LLM.
    """
    prompt = f"Extract only the technical skills from the following job description as a JSON array:\n{job_description}\nSkills:"

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
    outputs = model.generate(**inputs, max_length=150)
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)

    try:
        import json
        skills_list = json.loads(result)
    except:
        skills_list = [s.strip() for s in result.split(",")]

    return [s.lower() for s in skills_list]

def score_resume(parsed_resume: dict, job_description: str) -> dict:
    """
    Score the resume against the job description.
    """
    resume_skills = resume_utils.get_resume_skills(parsed_resume)
    jd_skills = extract_skills_from_jd(job_description)

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
