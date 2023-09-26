from sqlalchemy import Column, Integer, String
from ..database import Base

class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    name = Column(String(25), index=True, nullable=False)
    description = Column(String(255))