from core.dataset import save_sample

def analyze_log(log_obj):

    log = log_obj.get("result", {}).get("log", "")

    success = 0

    if "panic" in log.lower():
        success = 0

    elif "boot success" in log.lower():
        success = 1

    # 📊 SAVE TO DATASET (REAL LEARNING)
    save_sample(
        features=[50, 50, 50],  # placeholder features
        label=success
    )

    return success
