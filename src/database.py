from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = os.getenv(
  "DATABASE_URL", 
  "postgresql://nitish@localhost:5432/expense-tracker"
  )

engine = create_engine(
  SQLALCHEMY_DATABASE_URL,
  pool_size=10, # Connection pool size
  max_overflow=20, # Max Connections beyond pool size
  pool_pre_ping=True # verify connections before using them
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()