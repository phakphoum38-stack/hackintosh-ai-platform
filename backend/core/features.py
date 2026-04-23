# backend/core/features.py

def extract_features(config):

    return [
        config.get("acpi_score", 50) / 100,
        config.get("gpu_score", 50) / 100,
        config.get("usb_score", 50) / 100
    ]
