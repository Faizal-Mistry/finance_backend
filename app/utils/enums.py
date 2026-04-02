from enum import Enum

class TransactionType(str, Enum):
    income = "income"
    expense = "expense"

class UserRole(str, Enum):
    viewer = "viewer"
    analyst = "analyst"
    admin = "admin"