from sqlalchemy import Column, Integer, String
from ..database import Base

class Action_Type(Base):
    __tablename__ = 'action_types'

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    name = Column(String(30), nullable=False)