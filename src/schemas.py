from pydantic import BaseModel, EmailStr, validator
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    name: str
    password: str

    @validator('password')
    def validate_password(cls, v):
        # Check password length in bytes
        if len(v.encode('utf-8')) > 72:
            raise ValueError('password must be less than 72 bytes when encoded in utf-8')
        # Check minimum length
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        return v

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