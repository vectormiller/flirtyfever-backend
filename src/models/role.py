# Third party imports
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

# Local application imports
from ..database import Base

class Role(Base):
    __tablename__ = 'roles'
    
    id = Column(Integer, autoincrement=True, index=True, primary_key=True, unique=True)
    name = Column(String(25), doc='Name of the role', nullable=False)
    description = Column(String(255), doc='Description of the role', nullable=True)

    users = relationship('User', back_populates='role')
