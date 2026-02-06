from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

# Placeholder SQLite database for future extensions (e.g. precomputed data).
SQLALCHEMY_DATABASE_URL = "sqlite:///./strategy_visualizer.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator[Session, None, None]:
    """
    Dependency that yields a database session.

    Currently unused, but provided for future persistence needs.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

