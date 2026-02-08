from anthropic import Anthropic
from app.config import Config
from datetime import datetime


class LLMService:
    def __init__(self):
        self.client = Anthropic(api_key=Config.ANTHROPIC_API_KEY)
        self.model = Config.MODEL
        self.temperature = Config.TEMPERATURE
        self.max_tokens = Config.MAX_TOKENS

    def get_formatted_date(self) -> str:
        """Get today's date in 'Month Day, Year' format."""
        return datetime.now().strftime("%B %d, %Y")

    def generate_diary_novel(self, user_input: str, system_prompt: str = None, feedback: str = None) -> str:
        """
        Generate a diary-style novel from user input.
        
        Args:
            user_input: The conversation or notes to transform
            system_prompt: Custom system prompt (optional)
            feedback: User feedback for refinement (optional)
        """
        if system_prompt is None:
            system_prompt = """You are a talented ghostwriter that transforms casual conversations and notes 
into beautiful, literary diary entries. Transform the user's input into a diary-style narrative 
that is emotionally resonant, well-written, and captures the essence of what they're describing. 
Write in first person as if it's a diary entry. Start with the date in this format: **[Date]**"""

        # Build the prompt with optional feedback
        if feedback:
            full_prompt = f"""Original input: {user_input}

User feedback on previous version: {feedback}

Please regenerate the diary entry addressing this feedback."""
        else:
            full_prompt = user_input

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
