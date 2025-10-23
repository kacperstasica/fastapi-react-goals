import os

from dotenv import load_dotenv
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from logging_config import logger


load_dotenv()


async def connect_db(app: FastAPI) -> None:
    """Connect to MongoDB and store in app state"""
    try:
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
    if hasattr(app.state, "mongo_client"):
        app.state.mongo_client.close()
        logger.info("CLOSED MONGODB CONNECTION")
