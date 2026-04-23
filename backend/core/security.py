import jwt
from datetime import datetime, timedelta

SECRET = "SECRET_KEY"

def create_token(data: dict):

    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(days=1)

    return jwt.encode(payload, SECRET, algorithm="HS256")
