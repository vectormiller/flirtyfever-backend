# Standard library imports
from uuid import uuid4

# Third party imports
from sqlalchemy import Column, ForeignKey, Identity, Integer, String, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

# Local application imports
from ..database import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(uuid4(as_uuid=True), index=True, nullable=False, primary_key=True, unique=True)
    username = Column(String(25), index=True, nullable=False)
    description = Column(String(255), nullable=True)
    role_id = Column(Identity, ForeignKey("roles.id"), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
    phone_number = Column(Integer, nullable=False, unique=True)
    gender_id = Column(Identity, ForeignKey("genders.id"), nullable=False)
    city_id = Column(Identity, ForeignKey("cities.id"), nullable=False)
    rating = Column(Integer, default=30, nullable=False)
    age = Column(Integer, nullable=False)
    

    role = relationship('Role', back_populates='users')
    gender = relationship('Gender', back_populates='users')
    city = relationship('City', back_populates='users')
    user_images = relationship('UserImage', back_populates='user')
    
    actions = relationship('Action', foreign_keys='[Actions.from_id, Actions.to_id]', back_populates="user")
    from_actions = relationship('Action', foreign_keys='[Actions.from_id]', back_populates='from_user')
    to_actions = relationship('Action', foreign_keys='[Actions.to_id]', back_populates='to_user')
