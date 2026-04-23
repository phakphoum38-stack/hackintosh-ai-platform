from fastapi import APIRouter
from backend.core.queue import push_job

router = APIRouter()

@router.post("/submit")
def submit_job(config: dict):

    push_job(config)

    return {
        "status": "queued",
        "config": config
    }
