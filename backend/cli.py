#!/usr/bin/env python3
from app.services.llm_service import LLMService


def main():
    """Simple CLI to test the agent."""
    llm = LLMService()

    print("\n🎭 Welcome to Chronicle Weaver - AI Ghostwriter")
    print("=" * 50)
    print("Transform your conversations into literary diary entries!\n")

    while True:
        print("\nOptions:")
        print("1. Convert conversation to diary novel")
        print("2. Exit")

        choice = input("\nChoose an option (1-2): ").strip()

        if choice == "1":
            print("\n📝 Enter your conversation or notes (type 'END' on a new line when done):")
            lines = []
            while True:
                line = input()
                if line.strip().upper() == "END":
                    break
                lines.append(line)
            user_input = "\n".join(lines)

            if user_input.strip():
                print("\n✨ Generating your diary novel...\n")
                result = llm.generate_diary_novel(user_input)
                print("---\n" + result + "\n---")

                # Refinement loop
                while True:
                    feedback = input("\n💭 Did I capture the mood correctly? (yes/no/feedback): ").strip().lower()

                    if feedback in ["yes", "y"]:
                        print("✅ Great! Your diary entry is ready.")
                        break
                    elif feedback in ["no", "n"]:
                        print("\n📝 Please tell me what to improve:")
                        improvement = input("> ").strip()
                        if improvement:
                            print("\n✨ Regenerating with your feedback...\n")
                            result = llm.generate_diary_novel(user_input, feedback=improvement)
                            print("---\n" + result + "\n---")
                    else:
                        # Treat as feedback
                        print("\n✨ Regenerating with your feedback...\n")
                        result = llm.generate_diary_novel(user_input, feedback=feedback)
                        print("---\n" + result + "\n---")
            else:
                print("❌ No input provided.")

        elif choice == "2":
            print("\n👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
