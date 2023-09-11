from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLACLHEMY_URL = "postgresql+psycopg2://postgres:admin@localhost:5432/flirtyfever"

engine = create_engine(
    SQLACLHEMY_URL
    )
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()