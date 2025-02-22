# Simple AI Voice Assistant

A simple AI Voice Assistant backend built with FastAPI. This application accepts text input (simulating voice commands), processes the input using either basic keyword matching or the Google Gemini API for advanced responses, logs interactions to a MongoDB database (optional), and serves a simple web UI for user interaction.

---

## Features

- **FastAPI Backend:** Asynchronous API server using FastAPI.
- **Google Gemini API Integration:** Generates dynamic responses using Google Gemini generative AI.
- **Fallback Mechanism:** Uses basic keyword matching if the Gemini API key is not provided.
- **MongoDB Integration (Optional):** Logs user interactions to a MongoDB Atlas database.
- **Web UI:** A simple HTML interface served at the root endpoint.
- **Detailed Logging:** Provides comprehensive logs for debugging and monitoring.

---

## Prerequisites

- **Python 3.8+** installed on your system.
- **MongoDB Atlas Account (Optional):** To log interactions, create a cluster and obtain your connection URI.
- **Google Gemini API Key:** Obtain your API key from Google for accessing the Gemini generative AI service.

---

## Setup Instructions

### 1. Clone the Repository
git clone <repository_url>
cd ai-voice-assistant

### 2. Create and Activate a Virtual Environment

### On Linux/macOS:
python -m venv venv
source venv/bin/activate

### On Windows:
python -m venv venv
venv\Scripts\activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Set Up Environment Variables
Set the following environment variables:

MONGODB_URI (optional): Your MongoDB connection URI.
GEMINI_API_KEY (optional) : Your Google Gemini API key in the code header.

### On Linux/macOS:
export MONGODB_URI="your_mongodb_connection_uri"
export GEMINI_API_KEY="your_gemini_api_key"

### On Windows (Command Prompt):
set MONGODB_URI="your_mongodb_connection_uri"
set GEMINI_API_KEY="your_gemini_api_key"

### 5. Run the Application
Start the FastAPI server with uvicorn:

uvicorn main:app --reload
The server will be running at http://0.0.0.0:8000/.

### 6. Interact with the Application
Web UI: Open your browser and navigate to http://localhost:8000/ to use the simple interface(recommended).
API Endpoint: Test the /process endpoint using a tool like curl or Postman.

Example using curl:
curl -X POST "http://localhost:8000/process" \
-H "Content-Type: application/json" \
-d '{"text": "Tell me about Harry Potter"}'
