from backend.core.queue import push_job

def submit_job(config: dict):

    push_job(config)

    return {
        "status": "queued",
        "config": config
    }
