import os
from langchain_groq import ChatGroq

def get_groq_llm():
    """Initializes and returns the Groq language model."""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY is missing. Set it in the .env file.")
    return ChatGroq(model="qwen/qwen3-32b", api_key=api_key)
