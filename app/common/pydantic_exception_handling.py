from typing import Any
from pydantic import ValidationError
from nexios.http import Request,Response
from .response_format import wrap_response
async def handle_pydantic_validation_error(request: Request,  response :Response, exc: ValidationError) -> Any:
    """
    Handles Pydantic validation errors raised during request parsing.

    Args:
        request: The incoming HTTP request.
        exc: The Pydantic ValidationError that was raised.

    Returns:
        A 400 Bad Request response with the error message.
    """
    return response.json(wrap_response(data=exc.errors(), status=422),status_code=422)