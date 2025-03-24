from nexios.http import Request, Response
from app.common.response_format import wrap_response
from nexios.auth.backends.jwt import create_jwt
from ._utils.checks import authenticate_credentials
from ._utils.token_utils import get_user_from_token, rotate_tokens
from app.dto.auth.user_account_login_dto import UserAccountLoginDTO
from datetime import datetime,timedelta
from nexios.config import get_config
from nexios.logging import create_logger
logger = create_logger("auth_token_management")
async def issue_access_refresh_token(req :Request, res :Response):
    config = get_config()
    request_body = await req.json
    validate_data = UserAccountLoginDTO(**request_body)
    is_auth, user = await authenticate_credentials(**validate_data.model_dump())
    
    if not is_auth:
        return res.json(wrap_response(status=400),status_code=400)
    
    
    access_token_payload = {
        "user_id": user.id,
        "exp": datetime.utcnow() + timedelta(days=1)
    }
    refresh_token_payload = {
        "user_id": user.id,
        "exp": datetime.utcnow() + timedelta(days=30)
    }
    assert config.secret_key
    access_token = create_jwt(access_token_payload, config.secret_key)
    refresh_token = create_jwt(refresh_token_payload, config.secret_key)
    if config.env == "dev":
        return res.json(wrap_response(
            data={
                "access_token": create_jwt(access_token_payload, config.secret_key),
                "refresh_token": create_jwt(refresh_token_payload, config.secret_key)
            }
        ))
    
    
    res = res.json(wrap_response(
        message="Token Issued Successfully",
    ))
    res.set_cookie("access_token", access_token, httponly=True,secure=True, samesite="Lax")
    res.set_cookie("refresh_token", refresh_token, httponly=True,secure=True, samesite="Lax")
    return res



async def refresh_access_token(req :Request, res :Response):
    config = get_config()
    refresh_token = req.headers.get("refresh_token")
    if not refresh_token:
        logger.error("No Refresh Token Provided")
        return res.json(wrap_response(status=400),status_code=400)
    user = await get_user_from_token(refresh_token)
    if not user:
        logger.error("Invalid Refresh Token")
        return res.json(wrap_response(status=400),status_code=400)
    tokens = await rotate_tokens(user)
    if config.env == "dev":
        return res.json(wrap_response(data=tokens))
    res = res.json(wrap_response(
        message="Token Refreshed Successfully",
    ))
    res.set_cookie("access_token", tokens["access_token"], httponly=True,secure=True, samesite="Lax")
    res.set_cookie("refresh_token", tokens["refresh_token"], httponly=True,secure=True, samesite="Lax")
    return res