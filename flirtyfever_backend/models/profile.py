from sqlalchemy import Column, Integer, ForeignKey
from uuid import uuid4
from ..database import Base

class Profile(Base):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    user_id = Column(uuid4, ForeignKey("user.id"), nullable=False)
    priority = Column(Integer)
