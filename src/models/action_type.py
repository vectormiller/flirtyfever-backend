# Third party imports
from sqlalchemy import Column, Identity, Integer, String

# Local application imports
from ..database import Base

class Action_Type(Base):
    __tablename__ = 'action_types'
    
    id = Column(Identity, index=True, primary_key=True)
    name = Column(String(25), nullable=False)
    description = Column(String(255), nullable=True)
