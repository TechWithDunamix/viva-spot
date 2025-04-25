from typing import Dict, List
from typing import Any
from nexios.routing import Router,Routes
from pydantic import create_model
from app.dto.auth.user_base_account_dto import UserBaseAccountDTO
from .register_new_user import register_new_user
from .token_managements import issue_access_refresh_token,refresh_access_token 
router = Router(prefix="/auth", tags=["auth"])



router.add_route(Routes(
    path="/register",
    methods=["POST"],
    handler=register_new_user,
    request_model=UserBaseAccountDTO,
    description="Register a new user",
    summary="Register a new user account",
    responses={
        200 : create_model(
            "RegisterUserResponse",
            message=(str, "User registered successfully!"),
            user_id=(int, "ID of the registered user"),
            email=(str, "Email of the registered user"),
            username=(str, "Username of the registered user")
        ),
        422 : create_model(
            "RegisterUserErrorResponse",
            success=(bool, False),
            message=(str, "UnProcessable Entity"),
            errors = (List[Dict[str, str]], [{"loc": ["body", "email"], "msg": "value is not a valid email address", "type": "value_error.email"}]),
        )
    }


))


router.add_route(
    Routes(
        path="/token/new",
        methods=["POST"],
        handler=issue_access_refresh_token
        
    )
)

router.add_route(
    Routes(
        path="/token/refresh",
        methods=["POST"],
        handler=refresh_access_token
    )
)