# backend/core/infer.py

import torch
from core.model_registry import load_latest_model
from core.features import extract_features

# โหลดโมเดลล่าสุด
model = load_latest_model()

def predict(config):
    """
    รับ config (CPU/GPU/USB)
    แล้วคืนค่าโอกาส boot สำเร็จ
    """

    # 🧠 แปลง config → feature vector
    x = extract_features(config)

    x = torch.tensor(x, dtype=torch.float32)

    with torch.no_grad():
        score = model(x).item()

    return {
        "boot_success_probability": round(score * 100, 2)
    }
