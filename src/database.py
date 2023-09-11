"""
    Database Utility Functions

    This module provides utility functions for working with a database using SQLAlchemy.

    Functions:
        - get_db: Creates and manages a database connection session.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from settings import settings

SQLACLHEMY_URL = str(settings.DB_URL)

engine = create_engine(
    SQLACLHEMY_URL
    )
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    """
    Create and manage a database connection session.

    Returns:
        sqlalchemy.orm.Session: A SQLAlchemy session instance.
    """
    db = SessionLocal() # pylint: disable=invalid-name
    try:
        yield db
    finally:
        db.close()
