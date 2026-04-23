from core.dataset import save_sample

def analyze(log_obj):

    log = log_obj.get("result", {}).get("log", "")

    success = 1 if "success" in log else 0

    # save to dataset (learning loop)
    save_sample([50, 50, 50], success)

    return success
