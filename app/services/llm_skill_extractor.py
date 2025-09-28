from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

MODEL_NAME = "google/flan-t5-base"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

def extract_skills_from_jd(job_description: str) -> list:
    """
    Extract only technical skills from a JD as a list of strings.
    """
    from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
    import json

    MODEL_NAME = "google/flan-t5-base"
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

    prompt = f"Extract only the technical skills from the following job description as a JSON array:\n{job_description}\nSkills:"
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
    outputs = model.generate(**inputs, max_length=150)
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)

    try:
        skills_list = json.loads(result)
    except:
        skills_list = [s.strip() for s in result.split(",")]

    final_skills = []
    for skill in skills_list:
        if " and " in skill.lower():
            final_skills.extend([s.strip() for s in skill.split("and")])
        else:
            final_skills.append(skill.strip())

    final_skills = [s.lower() for s in final_skills if s]
    return final_skills
