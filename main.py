from fastapi import FastAPI
from pydantic import BaseModel
#from app.nlp import process_text  # Import NLP function

app = FastAPI(title="AI Voice Assistant")

# Define request body model
class VoiceInput(BaseModel):
    text: str

@app.post("/process-voice/")
def process_voice(input_data: VoiceInput):
    """Receives text input (simulating voice) and returns a response."""
    response = process_text(input_data.text)
    return {"response": response}

@app.get("/")
def home():
    return {"message": "Welcome to the AI Voice Assistant!"}
