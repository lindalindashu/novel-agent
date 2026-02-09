#!/usr/bin/env python3
"""Initialize the database with tables and a default user."""
from app.db import init_db, SessionLocal
from app.models import User, Entry

def main():
    """Initialize database and create default user."""
    print("🗄️  Initializing Chronicle Weaver database...")

    # Create tables
    init_db()
    print("✅ Database tables created")

    # Create default user if none exists
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.username == "default").first()
        if not user:
            user = User(username="default")
            db.add(user)
            db.commit()
            db.refresh(user)
            print(f"✅ Created default user: {user.username} (id={user.id})")
        else:
            print(f"ℹ️  Default user already exists: {user.username} (id={user.id})")

        # Show stats
        entry_count = db.query(Entry).count()
        print(f"📊 Current entries: {entry_count}")

    finally:
        db.close()

    print("\n🎉 Database initialization complete!")

if __name__ == "__main__":
    main()
