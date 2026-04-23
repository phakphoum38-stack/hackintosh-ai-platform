import redis
import json
import time

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

def run_qemu_boot(config):
    # placeholder for real VM execution
    return {
        "log": "boot success simulated",
        "success": 1
    }


def vm_loop():

    while True:

        try:
            job = r.brpop("vm_jobs", timeout=10)

            if not job:
                continue

            _, raw = job
            config = json.loads(raw)

            result = run_qemu_boot(config)

            r.lpush("logs", json.dumps({
                "config": config,
                "result": result
            }))

        except Exception as e:

            r.lpush("logs", json.dumps({
                "error": str(e)
            }))

            time.sleep(2)
