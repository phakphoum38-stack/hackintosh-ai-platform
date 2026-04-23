# backend/vm/feedback.py

from core.dataset import save_sample

def vm_feedback_update(config, boot_result):

    success = boot_result["success"]

    # 🔁 update tuning strategy
    if not success:

        config["tuning"] = "compatibility_mode"
        config["gpu_mode"] = "fallback_framebuffer"
        config["acpi_mode"] = "patch_required"

    else:

        config["tuning"] = "performance_mode"
        config["gpu_mode"] = "native"
        config["acpi_mode"] = "clean"

    # 📊 THIS IS THE LEARNING PART (สำคัญมาก)
    save_sample(
        features=[
            config.get("acpi_score", 50) / 100,
            config.get("gpu_score", 50) / 100,
            config.get("usb_score", 50) / 100
        ],
        label=1 if success else 0
    )

    return config
