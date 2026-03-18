import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Settings:
    SERVER_PORT: int = int(os.getenv("SERVER_PORT", "8080"))
    APP_NAME: str = os.getenv("APP_NAME", "llm-multiroute")
    # OpenAI compatible API base URL (e.g., http://localhost:11434 for Ollama)
    OPENAI_BASE_URL: str = os.getenv("OPENAI_BASE_URL", "https://openrouter.ai/api/v1")
    OPENAI_TEMPERATURE: float = float(os.getenv("OPENAI_TEMPERATURE", "0.7"))
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "ollama")

    # Per-route model assignments (read from environment)
    OPENAI_MODEL_CLASSIFY: str = os.getenv("OPENAI_MODEL_CLASSIFY", "stepfun/step-3.5-flash:free")
    OPENAI_MODEL_SENTIMENT: str = os.getenv("OPENAI_MODEL_SENTIMENT", "z-ai/glm-4.5-air:free")
    OPENAI_MODEL_SUMMARIZE: str = os.getenv("OPENAI_MODEL_SUMMARIZE", "nvidia/nemotron-3-super-120b-a12b:free")
    OPENAI_MODEL_INTENT: str = os.getenv("OPENAI_MODEL_INTENT", "arcee-ai/trinity-large-preview:free")


settings = Settings()
