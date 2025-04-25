from ast import Dict
import re
from typing import Any
from nexios.http import Request, Response
from app.models import Users
from app.dto.auth.user_base_account_dto import UserBaseAccountDTO
from ._utils.checks import email_exists
from ._utils.handlers import handle_user_account_check_errors
from ._utils.exceptions import UserAccountCreationCheckExcetiption
from app.common.wrap_exception import wrap_exception
from ._utils.token_utils import rotate_tokens

@wrap_exception(exception = UserAccountCreationCheckExcetiption, handler = handle_user_account_check_errors)
async def register_new_user(request: Request, response :Response) -> Any:
    
    request_data :Dict[str, Any] = await request.json
    user_data = UserBaseAccountDTO(**request_data)
    await email_exists(email = user_data.email)
    user = await Users.manager.create_account(**user_data.model_dump())
    response = response.json({
        "message": "User registered successfully!",
        "user_id": user.id,
        "email": user.email,
    })
    tokens = rotate_tokens(user = user)
    response.set_cookie(
        key = "access_token",
        value = tokens["access_token"],
        httponly = True,
        secure = True,
        samesite = "None",
        max_age = 60 * 60 * 24 * 30, # 30 days
    )
    response.set_cookie(
        key = "refresh_token",
        value = tokens["refresh_token"],
        httponly = True,
        secure = True,

        samesite = "None",
        max_age = 60 * 60 * 24 * 30, # 30 days
    )
    return response

    
    