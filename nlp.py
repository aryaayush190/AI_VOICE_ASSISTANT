import openai
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def process_text(user_input: str):
    """Handles AI response generation with error handling."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_input}]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"OpenAI API Error: {e}")  # Print error for debugging
        return f"Error: {e}"

