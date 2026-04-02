from pydantic import BaseModel
from app.utils.enums import UserRole

class UserCreate(BaseModel):
    username: str
    role: UserRole

class UserResponse(UserCreate):
    id: int

    class Config:
        orm_mode = True