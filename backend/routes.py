from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException, status
from motor.core import AgnosticDatabase
from pymongo.errors import DuplicateKeyError

from models.goal import GoalCreate
from dependencies import get_valid_object_id, get_db
from logging_config import logger


router = APIRouter()


@router.get("/goals")
async def get_goals(db: AgnosticDatabase = Depends(get_db)) -> dict[str, list[dict[str, str]]]:
    """Fetch all goals from MongoDB"""
    logger.info("TRYING TO FETCH GOALS")
    
    try:
        goals_collection = db["goals"]
        cursor = goals_collection.find({})
        goals = await cursor.to_list(length=None)
        
        response_goals = [
            {"id": str(goal["_id"]), "text": goal["text"]}
            for goal in goals
        ]
        
        logger.info("FETCHED GOALS")
        return {"goals": response_goals}
    
    except Exception as err:
        logger.error("ERROR FETCHING GOALS")
        logger.error(str(err))
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to load goals."
        )


@router.post("/goals", status_code=status.HTTP_201_CREATED)
async def create_goal(
    goal: GoalCreate,
    db: AgnosticDatabase = Depends(get_db)
) -> dict[str, str | dict[str, str]]:
    """Create a new goal"""
    logger.info("TRYING TO STORE GOAL")
    
    try:
        goals_collection = db["goals"]
        goal_doc = {"text": goal.text}
        result = await goals_collection.insert_one(goal_doc)
        
        logger.info("STORED NEW GOAL")
        return {
            "message": "Goal saved",
            "goal": {
                "id": str(result.inserted_id),
                "text": goal.text
            }
        }
    
    except DuplicateKeyError:
        logger.warning(f"DUPLICATE GOAL ATTEMPT: {goal.text}")
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Goal '{goal.text}' already exists. Please add a different goal."
        )
    
    except Exception as err:
        logger.error("ERROR SAVING GOAL")
        logger.error(str(err))
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to save goal."
        )


@router.delete("/goals/{id}")
async def delete_goal(id: ObjectId = Depends(get_valid_object_id), db: AgnosticDatabase = Depends(get_db)) -> dict[str, str]:
    """Delete a goal by ID"""
    logger.info("TRYING TO DELETE GOAL")
    
    try:
        goals_collection = db["goals"]
        await goals_collection.delete_one({"_id": id})
        
        logger.info("DELETED GOAL")
        return {"message": "Deleted goal!"}
    
    except Exception as err:
        logger.error("ERROR DELETING GOAL")
        logger.error(str(err))
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete goal."
        )
