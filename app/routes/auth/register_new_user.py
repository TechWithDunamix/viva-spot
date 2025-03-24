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

@wrap_exception(exception = UserAccountCreationCheckExcetiption, handler = handle_user_account_check_errors)
async def register_new_user(request: Request, response :Response) -> Any:
    
    request_data :Dict[str, Any] = await request.json
    user_data = UserBaseAccountDTO(**request_data)
    await email_exists(email = user_data.email)
    await Users.manager.create_account(**user_data.model_dump())
    return response.json({"message": "User registered successfully!"})
    
    