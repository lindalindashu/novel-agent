"""Diary service with database persistence and context injection."""
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.user import User
from app.models.entry import Entry
from app.services.llm_service import LLMService


class DiaryService:
    """Service for managing diary entries with context-aware generation."""

    def __init__(self, db: Session):
        self.db = db
        self.llm = LLMService()

    def get_or_create_user(self, username: str = "default") -> User:
        """Get existing user or create if doesn't exist."""
        stmt = select(User).where(User.username == username)
        user = self.db.scalar(stmt)
        if not user:
            user = User(username=username)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
        return user

    def get_recent_entries(self, user_id: int, limit: int = 5) -> List[Entry]:
        """Fetch recent entries for context."""
        stmt = (
            select(Entry)
            .where(Entry.user_id == user_id)
            .order_by(Entry.created_at.desc())
            .limit(limit)
        )
        return list(self.db.scalars(stmt).all())

    def generate_diary_entry(
        self,
        user_input: str,
        username: str = "default",
        feedback: Optional[str] = None,
        context_limit: int = 3
    ) -> Entry:
        """
        Generate a diary entry with context from previous entries.

        Args:
            user_input: User's casual notes/conversation
            username: Username (default: "default")
            feedback: Optional feedback for refinement
            context_limit: Number of previous entries to include (default: 3)

        Returns:
            Entry: The generated and saved entry
        """
        # Get or create user
        user = self.get_or_create_user(username)

        # Fetch recent entries for context
        recent_entries = self.get_recent_entries(user.id, limit=context_limit)

        # Generate diary text (LLM handles context building)
        generated_text = self.llm.generate_diary_novel(
            user_input=user_input,
            previous_entries=recent_entries,
            feedback=feedback
        )

        # Save to database
        entry = Entry(
            user_id=user.id,
            raw_input=user_input,
            generated_diary=generated_text,
            entry_metadata={}
        )
        self.db.add(entry)
        self.db.commit()
        self.db.refresh(entry)

        return entry

    def get_entry(self, entry_id: int) -> Optional[Entry]:
        """Get a specific entry by ID."""
        stmt = select(Entry).where(Entry.id == entry_id)
        return self.db.scalar(stmt)

    def get_all_entries(self, username: str = "default", limit: Optional[int] = None) -> List[Entry]:
        """Get all entries for a user."""
        user = self.get_or_create_user(username)
        stmt = (
            select(Entry)
            .where(Entry.user_id == user.id)
            .order_by(Entry.created_at.desc())
        )
        if limit:
            stmt = stmt.limit(limit)
        return list(self.db.scalars(stmt).all())

    def delete_entry(self, entry_id: int) -> bool:
        """Delete an entry."""
        entry = self.get_entry(entry_id)
        if entry:
            self.db.delete(entry)
            self.db.commit()
            return True
        return False
