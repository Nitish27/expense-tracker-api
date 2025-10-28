from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class User(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True, index=True)
  email = Column(String, unique=True, index=True, nullable=False)
  name = Column(String, nullable=False)
  hashed_password = Column(String, nullable=False)
  created_at = Column(DateTime, default=datetime.utcnow)

  expenses = relationship("Expense", back_populates="owner")

class Expense(Base):
  __tablename__ = "expenses"

  id = Column(Integer, primary_key=True, index=True)
  amount = Column(Float, nullable=False)
  category = Column(String, nullable=False)
  description = Column(String, nullable=True)
  date = Column(DateTime, default=datetime.utcnow)
  user_id = Column(Integer, ForeignKey("users.id"))

  owner = relationship("User", back_populates="expenses")