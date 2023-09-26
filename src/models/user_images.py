# Standard library imports
from uuid import uuid4

# Third party imports
from sqlalchemy import Column, ForeignKey, Integer

# Local application imports
from ..database import Base

class UserImages(Base):
    __tablename__ = 'user_images'

    id = Column(uuid4(as_uuid=True), index=True, nullable=False, primary_key=True, unique=True)
    user_id = Column(uuid4(as_uuid=True), ForeignKey('users.id'), index=True, nullable=False)
    priority = Column(Integer, default=1, nullable=False)
