from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.models.database import get_db
from core.models import utils

tracker_router = APIRouter()

@tracker_router.post("/symptoms/")
def log_symptoms(fatigue: int, pain: int, other_symptoms:str, db: Session = Depends(get_db)):
    utils.save_symptom_log(db, fatigue=fatigue, pain=pain, other_symptoms=other_symptoms)
    return {"success": True, "message": "Symptoms logged successfully"}

@tracker_router.get("/progress/")
def get_progress(db: Session = Depends(get_db)):
    return utils.get_progress_data(db)