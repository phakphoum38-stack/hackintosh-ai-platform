from fastapi import FastAPI
from backend.auth.routes import router as auth_router
from backend.scheduler.job_router import router as job_router
from backend.billing.webhook import router as billing_router

app = FastAPI(title="AI SaaS Platform")

app.include_router(auth_router, prefix="/auth")
app.include_router(job_router, prefix="/jobs")
app.include_router(billing_router, prefix="/billing")

@app.get("/")
def root():
    return {"status": "AI SaaS running"}
