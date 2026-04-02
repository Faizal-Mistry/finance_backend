from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.services.summary_service import *
from app.utils.auth import require_role

router = APIRouter(prefix="/summary", tags=["Summary"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def summary(db: Session = Depends(get_db),
            role=Depends(require_role(["viewer","analyst","admin"]))):
    return get_summary(db)

@router.get("/category")
def category(db: Session = Depends(get_db),
             role=Depends(require_role(["analyst","admin"]))):
    return category_breakdown(db)

@router.get("/monthly")
def monthly(db: Session = Depends(get_db),
            role=Depends(require_role(["analyst","admin"]))):
    return monthly_summary(db)

@router.get("/recent")
def recent(db: Session = Depends(get_db),
           role=Depends(require_role(["viewer","analyst","admin"]))):
    return recent_transactions(db)