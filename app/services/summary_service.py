from sqlalchemy.orm import Session
from sqlalchemy import func, extract
from app.models.transaction import Transaction

def get_summary(db: Session):
    income = db.query(func.sum(Transaction.amount)).filter(Transaction.type == "income").scalar() or 0
    expense = db.query(func.sum(Transaction.amount)).filter(Transaction.type == "expense").scalar() or 0

    return {
        "total_income": income,
        "total_expense": expense,
        "balance": income - expense
    }

def category_breakdown(db: Session):
    data = db.query(
        Transaction.category,
        func.sum(Transaction.amount)
    ).group_by(Transaction.category).all()

    return [{"category": c, "total": t} for c, t in data]

def monthly_summary(db: Session):
    data = db.query(
        extract('month', Transaction.date),
        func.sum(Transaction.amount)
    ).group_by(extract('month', Transaction.date)).all()

    return [{"month": int(m), "total": t} for m, t in data]

def recent_transactions(db: Session, limit=5):
    data = db.query(Transaction).order_by(Transaction.date.desc()).limit(limit).all()
    return data