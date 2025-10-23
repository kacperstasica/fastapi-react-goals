import logging
import os

from dotenv import load_dotenv
from fastapi import FastAPI, Request
from motor.motor_asyncio import AsyncIOMotorClient
from motor.core import AgnosticDatabase


# Load environment variables from .env file (for local development)
load_dotenv()

logger = logging.getLogger("access")


async def connect_db(app: FastAPI) -> None:
    """Connect to MongoDB and store in app state"""
    try:
        # Get MongoDB URI from environment variable or use default for local development
        mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
        database_name = os.getenv("MONGO_DATABASE", "course-goals")
        
        app.state.mongo_client = AsyncIOMotorClient(mongo_uri)
        app.state.db = app.state.mongo_client[database_name]
        logger.info(f"CONNECTED TO MONGODB: {database_name}")
    except Exception as err:
        logger.error("FAILED TO CONNECT TO MONGODB")
        logger.error(str(err))
        raise


async def disconnect_db(app: FastAPI) -> None:
    """Close MongoDB connection"""
    if hasattr(app.state, "mongo_client"):
        app.state.mongo_client.close()
        logger.info("CLOSED MONGODB CONNECTION")


async def get_db(request: Request) -> AgnosticDatabase:
    """Dependency to get database from app state"""
    return request.app.state.db

