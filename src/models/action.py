# Standard library imports
from uuid import uuid4

# Third party imports
from sqlalchemy import Column, ForeignKey, Identity, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

# Local application imports
from ..database import Base

class Action(Base):
    __tablename__ = 'actions'
    
    id = Column(uuid4(as_uuid=True), index=True, nullable=False, primary_key=True, unique=True)
    from_id = Column(uuid4(as_uuid=True), ForeignKey('users.id'), nullable=False)
    to_id = Column(uuid4(as_uuid=True), ForeignKey('users.id'), nullable=False)
    type = Column(Identity, ForeignKey("action_types.id"), nullable=False)
    occurred_at = Column(TIMESTAMP, nullable=False, server_default=func.now())

    user = relationship('User', back_populates='actions')
    from_user = relationship('Users', foreign_keys='[from_id]', back_populates='from_actions')
    to_user = relationship('Users', foreign_keys='[to_id]', back_populates='to_actions')
