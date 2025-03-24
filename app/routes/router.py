from nexios.routing import Router
from .auth.router import router as auth_router
api_router = Router(prefix="/api/v1")


api_router.mount_router(auth_router)