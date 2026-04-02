from fastapi import Header, HTTPException
from app.utils.enums import UserRole

def require_role(allowed_roles):
    def role_checker(role: str = Header(...)):
        if role not in [r.value for r in UserRole]:
            raise HTTPException(status_code=400, detail="Invalid role")

        if role not in allowed_roles:
            raise HTTPException(status_code=403, detail="Access denied")

        return role
    return role_checker