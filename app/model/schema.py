from pydantic import BaseModel
from typing import List

class ExtractedData(BaseModel):
    skills: List[str]

class Resume(BaseModel):
    extracted_data: ExtractedData

class ResumeJobRequest(BaseModel):
    resume: Resume
    job_description: str
