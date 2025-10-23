from fastapi import HTTPException
from fastapi import status
from fastapi.params import Path
from bson import ObjectId


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
