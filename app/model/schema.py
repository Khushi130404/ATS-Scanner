from pydantic import BaseModel
from typing import List, Optional

class ResumeJobRequest(BaseModel):
    resume: dict
    job_description: str
    skills: Optional[List[str]] = None
