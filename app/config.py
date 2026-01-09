import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# ---------- LLM ----------
LLM_PROVIDER = "openai"  # hard-coded since you want OpenAI only

# ---------- OpenAI ----------
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")

# ---------- Safety Check ----------
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY is not set")
