from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

MODEL_NAME = "google/flan-t5-base"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

def extract_skills_from_jd(job_description: str) -> list:
    """
    Given a job description, return a list of required skills.
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

    return skills_list
