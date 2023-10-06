# Standard library imports
from uuid import uuid4

# Third party imports
from sqlalchemy import Column, ForeignKey, Integer, TIMESTAMP
from sqlalchemy.sql import func

# Local application imports
from ..database import Base

class Action(Base):
    __tablename__ = 'actions'
    
    id = Column(uuid4(as_uuid=True), index=True, nullable=False, primary_key=True, unique=True)
    from_id = Column(uuid4(as_uuid=True), ForeignKey('users.id'), nullable=False)
    to_id = Column(uuid4(as_uuid=True), ForeignKey('users.id'), nullable=False)
    type = Column(Integer, ForeignKey("action_types.id"), nullable=False)
    occurred_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
