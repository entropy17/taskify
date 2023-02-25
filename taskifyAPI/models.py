from sqlalchemy import Boolean, Column, Integer, String
from database import Base

class Task(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(Integer)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
