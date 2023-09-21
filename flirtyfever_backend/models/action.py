from sqlalchemy import Column, Integer, Boolean, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from uuid import uuid4
from ..database import Base

class Action(Base):
    __tablename__ = 'actions'

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    from_id = Column(uuid4, ForeignKey("user.id"), nullable=False)
    to_id = Column(uuid4, ForeignKey("user.id"), nullable=False)
    type = Column(Boolean)
    performed_at = Column(TIMESTAMP, server_default=func.now())