from fastapi import FastAPI
from app.api import routes

app = FastAPI(title="ATS Scanner", version="1.0.0")

app.include_router(routes.router)

@app.get("/")
def root():
    return {"message": "ATS Scanner is running 🚀"}
