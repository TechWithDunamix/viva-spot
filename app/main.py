from nexios import get_application
from nexios.logging import create_logger
from app.config import app_config
from app.db import init_db, close_db
from contextlib import asynccontextmanager
from nexios.static import StaticFilesHandler
from nexios.routing import Routes
import uvicorn
from pathlib import Path
from app.routes.index import router
from app.routes.router import api_router
from app.common.pydantic_exception_handling import handle_pydantic_validation_error,ValidationError

logging = create_logger("nexios")

@asynccontextmanager
async def app_lifespan(app):
    """
    Manages the application's lifecycle events.
    - Initializes the database when the app starts.
    - Cleans up resources (e.g., closes database connections) when the app shuts down.

    Args:
        app: The application instance. This is passed automatically by the framework.
    """
    logging.info("Starting Nexios App")
    await init_db()  
    yield  
    logging.info("Shutting down Nexios App")
    await close_db()  

app = get_application(config=app_config, lifespan=app_lifespan)

STATIC_FOLDER = Path(__file__).resolve().parent.parent / "static"

app.add_route(
    route=Routes(
        "/static/{path:path}",  
        handler=StaticFilesHandler(
            directory=STATIC_FOLDER  
        )
    )
)

app.mount_router(router=router)
app.mount_router(router=api_router)
app.add_exception_handler(ValidationError, handle_pydantic_validation_error)

# Entry point to run the application using Uvicorn
if __name__ == "__main__":
    """
    Runs the application using Uvicorn, an ASGI server.

    Args:
        app: The application instance to run.
        port: The port number on which the application will listen (default: 8000).
        host: The host address to bind the server to (default: "0.0.0.0").
    """
    uvicorn.run(app, port=8000, host="0.0.0.0")  # Run the app on all available interfaces