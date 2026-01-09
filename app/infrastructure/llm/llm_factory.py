from app.config import LLM_PROVIDER
from app.infrastructure.llm.openai_client import OpenAILLM


def get_llm():
    if LLM_PROVIDER == "openai":
        return OpenAILLM()
    else:
        raise ValueError(f"Unsupported LLM provider: {LLM_PROVIDER}")
