from sqlalchemy import Boolean, Column, Integer, String, Identity, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from ..database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    username = Column(String, index=True, nullable=False)
    description = Column(String(255))
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    phone_number = Column(Integer, unique=True, nullable=False)
    gender_id = Column(Integer, ForeignKey("genders.id"), nullable=False)
    city_id = Column(Integer, ForeignKey("cities.id"), nullable=False)
    rating = Column(Integer, server_default=30)
    age = Column(Integer, nullable=False)