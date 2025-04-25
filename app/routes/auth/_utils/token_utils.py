from datetime import datetime, timedelta
from nexios.auth.backends.jwt import create_jwt, decode_jwt
from nexios.config import get_config
from pytz import UTC
from app.models import Users

async def get_user_from_token(token):
    config = get_config()
    assert config.secret_key
    try:
        payload = decode_jwt(token, config.secret_key,algorithms=["HS256"])
        
    except Exception as e:
        return None
    return await Users.get_or_none(id=payload.get("user_id"))   
    
    
async def rotate_tokens(user :Users) -> dict[str,str]:
    config = get_config()
    access_token_payload = {
        "user_id": user.id,
        "exp": datetime.now(UTC) + timedelta(days=1)
    }
    refresh_token_payload = {
        "user_id": user.id,
        "exp": datetime.now(UTC) + timedelta(days=30)
    }
    assert config.secret_key, "Secret Key Not Found"
    return {
        "access_token": create_jwt(access_token_payload, config.secret_key),
        "refresh_token": create_jwt(refresh_token_payload, config.secret_key)
    }