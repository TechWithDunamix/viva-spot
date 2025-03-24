from tortoise import Tortoise
from app.config import db_config

async def init_db():
    """
    Initialize the database connection using the provided configuration.
    This function sets up the connection to the database and ensures
    the necessary tables are created if they do not already exist.
    """
    await Tortoise.init(
        config=db_config  # Load database configuration (e.g., host, port, credentials)
    )
    # Generate database schemas to create tables if they don't exist
    await Tortoise.generate_schemas()

async def close_db():
    """
    Close all active database connections.
    This function ensures that connections are properly terminated
    to avoid resource leaks or connection pool exhaustion.
    """
    await Tortoise.close_connections()