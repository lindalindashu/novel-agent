"""User model."""
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db import Base


class User(Base):
    """User model for Chronicle Weaver."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationship to entries
    entries = relationship("Entry", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}')>"
