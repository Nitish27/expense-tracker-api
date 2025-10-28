from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
  email: EmailStr
  name: str
  password: str

class UserResponse(BaseModel):
  id: int
  email: EmailStr
  name: str
  created_at: datetime

  class Config:
    from_attributes = True

class ExpenseCreate(BaseModel):
  amount: float
  category: str
  description: Optional[str] = None
  date: Optional[datetime] = None

class ExpenseResponse(BaseModel):
  id: int
  amount: float
  category: str
  description: Optional[str]
  date: datetime
  user_id: int

  class Config:
    from_attributes = True