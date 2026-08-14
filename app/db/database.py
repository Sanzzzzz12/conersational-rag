from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


# ==============================
# DATABASE CONFIGURATION
# ==============================

DATABASE_URL = "sqlite:///./app.db"


# Create database engine
engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread": False
    }
)


# Create database session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Base class for SQLAlchemy models
Base = declarative_base()


# ==============================
# DATABASE DEPENDENCY
# ==============================

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()