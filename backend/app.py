from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import connect_db, disconnect_db
from routes import router
from logging_config import setup_logger, LoggingMiddleware


logger = setup_logger()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_db(app)
    yield
    await disconnect_db(app)


app = FastAPI(lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type"],
)


app.add_middleware(LoggingMiddleware, logger=logger)


app.include_router(router)
