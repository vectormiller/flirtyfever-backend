# Third party imports
from sqlalchemy import Column, Identity, Integer, String
from sqlalchemy.orm import relationship

# Local application imports
from ..database import Base

class Gender(Base):
    __tablename__ = 'genders'
    
    id = Column(Identity, index=True, primary_key=True)
    name = Column(String(25), doc='Name of the gender', nullable=False)
    description = Column(String(255), doc='Description of the gender', nullable=True)

    users = relationship('User', back_populates='gender')
