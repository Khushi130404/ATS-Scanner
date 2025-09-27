# ATS-Scanner

A FastAPI-based project to calculate ATS (Applicant Tracking System) scores by comparing parsed resumes with job descriptions.  
Uses **hybrid NLP + ML techniques** (keyword matching + embeddings + optional LLM) for skill extraction and scoring.

## 📂 Project Structure

ATS-Scanner/
│── app/
│ │── main.py
│ │── api/routes.py
│ │── core/config.py
│ │── models/schema.py
│ │── services/ats_scoring.py
│ │── utils/text_utils.py
│── tests/
│── requirements.txt
│── README.md
│── .gitignore

## ⚡ Setup & Run

python -m venv venv
source venv/bin/activate # On Linux/Mac
venv\Scripts\activate # On Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
