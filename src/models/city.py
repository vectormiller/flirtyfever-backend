# Third party imports
from sqlalchemy import Column, Identity, Integer, String
from sqlalchemy.orm import relationship

# Local application imports
from ..database import Base

class City(Base):
    __tablename__ = 'cities'
    
    id = Column(Identity, index=True, primary_key=True)
    name = Column(String(25), doc='Name of the city', nullable=False)

    users = relationship('User', back_populates='city')
