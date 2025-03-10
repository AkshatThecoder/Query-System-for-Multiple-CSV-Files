import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Raise an error if the API key is missing
if not GROQ_API_KEY:
    raise ValueError("❌ GROQ_API_KEY is missing. Set it in the .env file.")
