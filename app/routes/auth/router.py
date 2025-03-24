from nexios.routing import Router,Routes
from .register_new_user import register_new_user
from .token_managements import issue_access_refresh_token,refresh_access_token
router = Router(prefix="/auth")



router.add_route(Routes(
    path="/register",
    methods=["POST"],
    handler=register_new_user
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