from typing import Annotated

from pydantic import BaseModel, field_validator


class GoalCreate(BaseModel):
    """Schema for creating a new goal"""
    text: str
    
    @field_validator('text')
    @classmethod
    def validate_text_not_empty(cls, v: str) -> str:
        if not v or v.strip() == "":
            raise ValueError("Invalid goal text.")
        return v

    class Config:
        json_schema_extra = {
            "example": {
                "text": "Learn FastAPI"
            }
        }


class GoalResponse(BaseModel):
    """Schema for goal response"""
    id: str
    text: str

    class Config:
        json_schema_extra = {
            "example": {
                "id": "507f1f77bcf86cd799439011",
                "text": "Learn FastAPI"
            }
        }

