from fastapi import FastAPI
from backend.scheduler.job_router import submit_job

app = FastAPI(title="AI SaaS API")

@app.get("/")
def root():
    return {"status": "running"}

@app.post("/build")
def build(config: dict):
    return submit_job(config)
