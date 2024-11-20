from fastapi import APIRouter, HTTPException
from core.models.llama3_1 import generate_recommedations
from typing import List
recommendation_router = APIRouter()


@recommendation_router.post("/")
def get_recommendation(symptoms: List[str]):
    try:
        recommendations = generate_recommedations(symptoms)
        return {"success": True, "recommendations": recommendations}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
