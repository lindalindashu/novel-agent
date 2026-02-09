"""LLM service for diary generation with Claude."""
from anthropic import Anthropic
from app.config import Config
from datetime import datetime
from typing import List, Optional


class LLMService:
    def __init__(self):
        self.client = Anthropic(api_key=Config.ANTHROPIC_API_KEY)
        self.model = Config.MODEL
        self.temperature = Config.TEMPERATURE
        self.max_tokens = Config.MAX_TOKENS

    def get_formatted_date(self) -> str:
        """Get today's date in 'Month Day, Year' format."""
        return datetime.now().strftime("%B %d, %Y")

    def build_context_from_entries(self, previous_entries: List) -> str:
        """
        Build context prompt from previous diary entries.

        Args:
            previous_entries: List of Entry objects or diary text strings

        Returns:
            Formatted context string for the prompt
        """
        if not previous_entries:
            return ""

        context_parts = ["PREVIOUS ENTRIES (for narrative continuity):"]

        # Reverse to show oldest first (chronological order)
        for entry in reversed(previous_entries):
            context_parts.append("---")
            # Handle both Entry objects and plain strings
            if hasattr(entry, 'generated_diary'):
                context_parts.append(entry.generated_diary)
            else:
                context_parts.append(str(entry))

        context_parts.append("---")
        return "\n".join(context_parts)

    def generate_diary_novel(
        self,
        user_input: str,
        previous_entries: Optional[List] = None,
        feedback: Optional[str] = None,
        system_prompt: Optional[str] = None
    ) -> str:
        """
        Generate a diary-style novel from user input.

        Args:
            user_input: The conversation or notes to transform
            previous_entries: List of previous Entry objects for context (optional)
            feedback: User feedback for refinement (optional)
            system_prompt: Custom system prompt (optional, will override default)

        Returns:
            Generated diary entry text
        """
        # Base system prompt
        if system_prompt is None:
            system_prompt = """You are a talented ghostwriter that transforms casual conversations and notes
into beautiful, literary diary entries. Transform the user's input into a diary-style narrative
that is emotionally resonant, well-written, and captures the essence of what they're describing.
Write in first person as if it's a diary entry. Start with the date in this format: **[Date]**"""

        # Add context if previous entries provided
        if previous_entries:
            context = self.build_context_from_entries(previous_entries)
            system_prompt = f"{system_prompt}\n\n{context}"

        # Build user prompt with optional feedback
        if feedback:
            full_prompt = f"""Original input: {user_input}

User feedback on previous version: {feedback}

Please regenerate the diary entry addressing this feedback."""
        else:
            full_prompt = user_input

        # Call Claude
        response = self.client.messages.create(
            model=self.model,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
            system=system_prompt,
            messages=[{"role": "user", "content": full_prompt}],
        )

        # Add date to the response if not already present
        text = response.content[0].text
        if "**" not in text[:20]:  # If date format not found at start
            date_str = self.get_formatted_date()
            text = f"**{date_str}**\n\n{text}"

        return text
