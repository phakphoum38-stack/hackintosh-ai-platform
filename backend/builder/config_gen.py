# backend/builder/config_gen.py

def generate_config(config, kexts):

    return {
        "PlatformInfo": {
            "CPU": config["cpu"],
            "GPU": config["gpu"]
        },
        "Kernel": {
            "Add": kexts
        }
    }
