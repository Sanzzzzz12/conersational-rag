from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from app.db.database import Base


# ==============================
# DOCUMENT MODEL
# ==============================

class Document(Base):

    __tablename__ = "documents"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    filename = Column(
        String,
        nullable=False
    )

    file_type = Column(
        String,
        nullable=False
    )

    chunking_strategy = Column(
        String,
        nullable=False
    )

    chunk_count = Column(
        Integer,
        nullable=False
    )

    uploaded_at = Column(
        DateTime,
        default=datetime.utcnow
    )


# ==============================
# INTERVIEW BOOKING MODEL
# ==============================

class InterviewBooking(Base):

    __tablename__ = "interview_bookings"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String,
        nullable=False
    )

    email = Column(
        String,
        nullable=False
    )

    date = Column(
        String,
        nullable=False
    )

    time = Column(
        String,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )