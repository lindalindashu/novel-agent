#!/usr/bin/env python3
from llm_service import LLMService


def main():
    """Simple CLI to test the agent."""
    llm = LLMService()

    print("\n🎭 Welcome to Chronicle Weaver - AI Ghostwriter")
    print("=" * 50)
    print("Transform your conversations into literary diary entries!\n")

    while True:
        print("\nOptions:")
        print("1. Convert conversation to diary novel")
        print("2. Extract entities from text")
        print("3. Exit")

        choice = input("\nChoose an option (1-3): ").strip()

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
            else:
                print("❌ No input provided.")

        elif choice == "2":
            print("\n📊 Enter text to extract entities (type 'END' on a new line when done):")
            lines = []
            while True:
                line = input()
                if line.strip().upper() == "END":
                    break
                lines.append(line)
            user_input = "\n".join(lines)

            if user_input.strip():
                print("\n🔍 Extracting entities...\n")
                result = llm.extract_entities(user_input)
                print("---\n" + result + "\n---")
            else:
                print("❌ No input provided.")

        elif choice == "3":
            print("\n👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
