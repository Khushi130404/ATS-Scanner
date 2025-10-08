# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from app.api import routes

# app = FastAPI(title="ATS Scanner", version="1.0.0")

# app.include_router(routes.router)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.get("/", tags=["Root"])
# def root():
#     """
#     Health check endpoint
#     """
#     return {
#         "message": "ATS Scanner API is running 🚀",
#         "status": "ok",
#         "version": "1.0.0"
#     }

#  Above is the actual code 
# Below we have dummy code

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="ATS Scanner API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

dummy_ats_data = {
    "ats_score": 60,
    "matched_skills": ["Kafka", "Sql", "Python", "Hive", "Hadoop", "Spark"],
    "missing_skills": ["HBase", "Sqoop"],
    "suggestions": {
        "score_analysis": "Your resume shows a strong 67% match against the provided Big Data Engineer job description...",
        "strengths_to_highlight": "Your resume's significant strengths lie in your proficiency with key Big Data technologies...",
        "missing_skills_advice": "Missing HBase and Sqoop. Consider highlighting experience with NoSQL or cloud platforms.",
        "general_improvements": "Populate your Experience & Projects sections. Clarify target role vs job description."
    }
}

@app.get("/", tags=["Root"])
def root():
    return {"message": "ATS Scanner API is running 🚀", "status": "ok", "version": "1.0.0"}

@app.post("/score", tags=["ATS"])
def get_ats_score():
    """
    Dummy endpoint for ATS scoring.
    Returns pre-defined ATS score and suggestions.
    """
    return dummy_ats_data
