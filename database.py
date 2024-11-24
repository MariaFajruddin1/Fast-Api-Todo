# database.py

from sqlalchemy import create_engine, Column, Integer, String, Boolean

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://mariafajruddin:MFmSv01Pqnyo@ep-restless-boat-a5sipi4m.us-east-2.aws.neon.tech/todo?sslmode=require"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    is_complete = Column(Boolean, index=True)