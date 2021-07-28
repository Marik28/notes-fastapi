import datetime as dt
import uuid

from sqlalchemy import (
    Column,
    Integer,
    String,
    TIMESTAMP,
    CheckConstraint,
    ForeignKey
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from .settings import settings

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(length=320), unique=True, nullable=False)
    username = Column(String(length=settings.username_max_length), unique=True, nullable=False)
    password_hash = Column(String)

    __table_args__ = (
        CheckConstraint(f"LENGTH(username) >= {settings.username_min_length}",
                        "username_min_length"),
    )


class Note(Base):
    __tablename__ = "notes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(length=settings.max_note_title_length), nullable=False)
    text = Column(String(length=settings.max_note_text_length), nullable=False)
    date_create = Column(TIMESTAMP, default=dt.datetime.utcnow, nullable=False)
    date_update = Column(TIMESTAMP, default=dt.datetime.utcnow, onupdate=dt.datetime.utcnow, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    owner = relationship("User", backref="notes")
