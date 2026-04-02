from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.schemas.transaction import *
from app.services.transaction_service import *
from app.utils.auth import require_role

router = APIRouter(prefix="/transactions", tags=["Transactions"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=TransactionResponse)
def create(tx: TransactionCreate,
           db: Session = Depends(get_db),
           role=Depends(require_role(["admin"]))):
    return create_transaction(db, tx)

@router.get("/", response_model=list[TransactionResponse])
def list_transactions(type: str = None,
                      category: str = None,
                      start_date: str = None,
                      end_date: str = None,
                      skip: int = 0,
                      limit: int = 10,
                      db: Session = Depends(get_db),
                      role=Depends(require_role(["viewer","analyst","admin"]))):
    return get_transactions(db, {
        "type": type,
        "category": category,
        "start_date": start_date,
        "end_date": end_date
    }, skip, limit)

@router.put("/{tx_id}", response_model=TransactionResponse)
def update(tx_id: int,
           tx_data: TransactionUpdate,
           db: Session = Depends(get_db),
           role=Depends(require_role(["admin"]))):
    tx = update_transaction(db, tx_id, tx_data)
    if not tx:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return tx

@router.delete("/{tx_id}")
def delete(tx_id: int,
           db: Session = Depends(get_db),
           role=Depends(require_role(["admin"]))):
    tx = delete_transaction(db, tx_id)
    if not tx:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return {"message": "Deleted"}