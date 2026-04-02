from pydantic import BaseModel, Field
from datetime import date
from app.utils.enums import TransactionType

class TransactionBase(BaseModel):
    amount: float = Field(gt=0)
    type: TransactionType
    category: str = Field(min_length=2)
    date: date
    notes: str | None = None

class TransactionCreate(TransactionBase):
    pass

class TransactionUpdate(TransactionBase):
    pass

class TransactionResponse(TransactionBase):
    id: int

    class Config:
        orm_mode = True