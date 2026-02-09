"""Entry model."""
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db import Base


class Entry(Base):
    """Diary entry model."""

    __tablename__ = "entries"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    raw_input = Column(Text, nullable=False)
    generated_diary = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), index=True)
    entry_metadata = Column(JSON, default={})

    # Relationship to user
    user = relationship("User", back_populates="entries")

    def __repr__(self):
        return f"<Entry(id={self.id}, user_id={self.user_id}, created_at={self.created_at})>"

    def to_dict(self):
        """Convert entry to dictionary."""
        return {
            "id": self.id,
            "user_id": self.user_id,
            "raw_input": self.raw_input,
            "generated_diary": self.generated_diary,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "metadata": self.entry_metadata or {}
        }
