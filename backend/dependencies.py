from fastapi import HTTPException
from fastapi import status
from fastapi.params import Path
from bson import ObjectId
from fastapi import Request
from motor.core import AgnosticDatabase


def get_valid_object_id(id: str = Path(...)) -> ObjectId:
    """
    Dependency to validate a string as a MongoDB ObjectId
    and convert it.
    """
    if not ObjectId.is_valid(id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"'{id}' is not a valid ObjectId format."
        )
    return ObjectId(id)


async def get_db(request: Request) -> AgnosticDatabase:
    """Dependency to get database from app state"""
    return request.app.state.db