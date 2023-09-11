from sqlalchemy import Boolean, Column, Integer, String, Identity
from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    name = Column(String, index=True)
    lastname = Column(String, index=True)
    middlename = Column(String, index=True) # TODO: Make it optional