import redis
import json
import subprocess

r = redis.Redis(host="redis", port=6379, decode_responses=True)

def run_qemu(config):

    # mock VM boot
    return {
        "success": 1,
        "log": "boot success"
    }

def loop():

    while True:

        job = r.brpop("vm_jobs")

        _, raw = job
        config = json.loads(raw)

        result = run_qemu(config)

        r.lpush("vm_results", json.dumps({
            "config": config,
            "result": result
        }))
