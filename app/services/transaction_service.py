from sqlalchemy.orm import Session
from app.models.transaction import Transaction

def create_transaction(db: Session, data):
    tx = Transaction(**data.dict())
    db.add(tx)
    db.commit()
    db.refresh(tx)
    return tx

def get_transactions(db: Session, filters, skip=0, limit=10):
    query = db.query(Transaction)

    if filters.get("type"):
        query = query.filter(Transaction.type == filters["type"])

    if filters.get("category"):
        query = query.filter(Transaction.category == filters["category"])

    if filters.get("start_date"):
        query = query.filter(Transaction.date >= filters["start_date"])

    if filters.get("end_date"):
        query = query.filter(Transaction.date <= filters["end_date"])

    return query.offset(skip).limit(limit).all()

def get_transaction_by_id(db, tx_id):
    return db.query(Transaction).get(tx_id)

def update_transaction(db: Session, tx_id, data):
    tx = get_transaction_by_id(db, tx_id)
    if not tx:
        return None

    for key, value in data.dict().items():
        setattr(tx, key, value)

    db.commit()
    db.refresh(tx)
    return tx

def delete_transaction(db: Session, tx_id):
    tx = get_transaction_by_id(db, tx_id)
    if not tx:
        return None

    db.delete(tx)
    db.commit()
    return tx