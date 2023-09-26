from sqlalchemy import Column, Integer, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from uuid import uuid4
from ..database import Base

class Action(Base):
    __tablename__ = 'actions'

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    from_id = Column(uuid4, ForeignKey("users.id"), nullable=False)
    to_id = Column(uuid4, ForeignKey("users.id"), nullable=False)
    type = Column(Integer, ForeignKey("action_types.id"), nullable=False)
    performed_at = Column(TIMESTAMP, server_default=func.now())