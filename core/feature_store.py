# core/feature_store.py

def extract_features(config):

    return {
        "acpi": config.get("acpi_score", 50),
        "gpu": config.get("gpu_score", 50),
        "usb": config.get("usb_score", 50)
    }
