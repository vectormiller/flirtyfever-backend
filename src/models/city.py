from sqlalchemy import Column, Integer, String
from ..database import Base

class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    name = Column(String(25), index=True, nullable=False)