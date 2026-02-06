from anthropic import Anthropic
from config import Config


class LLMService:
    def __init__(self):
        self.client = Anthropic(api_key=Config.ANTHROPIC_API_KEY)
        self.model = Config.MODEL
        self.temperature = Config.TEMPERATURE
        self.max_tokens = Config.MAX_TOKENS

    def generate_diary_novel(self, user_input: str, system_prompt: str = None) -> str:
        """
        Generate a diary-style novel from user input.
        """
        if system_prompt is None:
            system_prompt = """You are a talented ghostwriter that transforms casual conversations and notes 
into beautiful, literary diary entries. Transform the user's input into a diary-style narrative 
that is emotionally resonant, well-written, and captures the essence of what they're describing. 
Write in first person as if it's a diary entry dated today."""

        response = self.client.messages.create(
            model=self.model,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
            system=system_prompt,
            messages=[{"role": "user", "content": user_input}],
        )

        return response.content[0].text

    def extract_entities(self, text: str) -> dict:
        """
        Extract entities (who), events (what), and emotions (how) from text.
        """
        system_prompt = """You are an expert at extracting key information from conversations. 
Extract and return a JSON object with the following structure:
{
  "entities": [{"name": "...", "type": "person|place|thing", "role": "..."}],
  "events": [{"action": "...", "time": "...", "significance": "high|medium|low"}],
  "emotions": [{"feeling": "...", "intensity": "1-10", "trigger": "..."}]
}"""

        response = self.client.messages.create(
            model=self.model,
            max_tokens=self.max_tokens,
            temperature=0.3,  # Lower temperature for structured output
            system=system_prompt,
            messages=[{"role": "user", "content": f"Extract information from this text:\n\n{text}"}],
        )

        return response.content[0].text
