import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
    MODEL = "claude-opus-4-1-20250805"
    MAX_TOKENS = 2048
    TEMPERATURE = 0.7
