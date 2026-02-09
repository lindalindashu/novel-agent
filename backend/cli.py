#!/usr/bin/env python3
from app.db import SessionLocal
from app.services.diary_service import DiaryService


def main():
    """CLI with database persistence and context."""
    print("\n🎭 Welcome to Chronicle Weaver - AI Ghostwriter")
    print("=" * 50)
    print("Transform your conversations into literary diary entries!\n")

    db = SessionLocal()
    service = DiaryService(db)

    try:
        # Show recent entries
        recent = service.get_all_entries(limit=5)
        print(f"📚 You have {len(recent)} recent entries in your chronicle\n")

        while True:
            print("\nOptions:")
            print("1. Write new diary entry")
            print("2. View recent entries")
            print("3. Exit")

            choice = input("\nChoose an option (1-3): ").strip()

            if choice == "1":
                print("\n📝 Enter your notes (type 'END' on a new line when done):")
                lines = []
                while True:
                    line = input()
                    if line.strip().upper() == "END":
                        break
                    lines.append(line)
                user_input = "\n".join(lines)

                if user_input.strip():
                    print("\n✨ Generating your diary entry with context...\n")
                    entry = service.generate_diary_entry(user_input)
                    print("---\n" + entry.generated_diary + "\n---")

                    # Refinement loop
                    while True:
                        feedback = input("\n💭 Satisfied with this entry? (yes/no/feedback): ").strip().lower()

                        if feedback in ["yes", "y"]:
                            print(f"✅ Entry #{entry.id} saved to your chronicle!")
                            break
                        elif feedback in ["no", "n"]:
                            print("\n📝 What should I change?")
                            improvement = input("> ").strip()
                            if improvement:
                                print("\n✨ Regenerating...\n")
                                # Delete old entry and create new one with feedback
                                service.delete_entry(entry.id)
                                entry = service.generate_diary_entry(user_input, feedback=improvement)
                                print("---\n" + entry.generated_diary + "\n---")
                        else:
                            # Treat as feedback
                            print("\n✨ Regenerating...\n")
                            service.delete_entry(entry.id)
                            entry = service.generate_diary_entry(user_input, feedback=feedback)
                            print("---\n" + entry.generated_diary + "\n---")
                else:
                    print("❌ No input provided.")

            elif choice == "2":
                entries = service.get_all_entries(limit=10)
                if not entries:
                    print("\n📭 No entries yet. Start writing!")
                else:
                    print(f"\n📖 Your Recent Entries ({len(entries)}):\n")
                    for e in entries:
                        date = e.created_at.strftime("%Y-%m-%d %H:%M")
                        preview = e.generated_diary[:100].replace("\n", " ")
                        print(f"  [{e.id}] {date}")
                        print(f"      {preview}...\n")

            elif choice == "3":
                print("\n👋 Goodbye!")
                break

            else:
                print("❌ Invalid choice. Please try again.")

    finally:
        db.close()


if __name__ == "__main__":
    main()
