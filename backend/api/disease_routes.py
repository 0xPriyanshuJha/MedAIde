from fastapi import APIRouter, HTTPException
from typing import List

disease_router = APIRouter()

# Example disease data
disease_db = {
    "diabetes": {"symptoms": ["fatigue", "excess thirst"], "management": ["diet control", "medication"]},
    "hypertension": {"symptoms": ["headache", "dizziness"], "management": ["exercise", "low-salt diet"]},
}

@disease_router.get("/{disease_name}")
def get_disease_info(disease_name: str):
    disease_info = disease_db.get(disease_name.lower())
    if not disease_info:
        raise HTTPException(status_code=404, detail="Disease not found")
    return {"disease": disease_name, "info": disease_info}
