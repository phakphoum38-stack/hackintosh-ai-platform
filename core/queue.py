import redis
import json

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

QUEUE_NAME = "vm_jobs"

def push_job(config):

    r.lpush(QUEUE_NAME, json.dumps(config))


def get_job():

    return r.brpop(QUEUE_NAME)
