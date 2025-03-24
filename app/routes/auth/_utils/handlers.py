from typing import Any
from nexios.http import Response, Request
from app.common.response_format import wrap_response
from .exceptions import UserAccountCreationCheckExcetiption
def handle_user_account_check_errors(request: Request, response :Response, exception :UserAccountCreationCheckExcetiption) -> Any:
    
    return response.json(
        wrap_response(
            status = 400,
            message = exception.message,
            data = exception.data,
            
        ),
        status_code=400
    )