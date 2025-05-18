from dotenv import load_dotenv
import os

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_api_url = os.getenv("GEMINI_API_URL")
gemini_api_model = os.getenv("GEMINI_API_MODEL")


if not gemini_api_key or not gemini_api_url or not gemini_api_model:
    print("Please set the environment variables GEMINI_API_KEY, GEMINI_API_URL, and GEMINI_API_MODEL.")
    exit(1)
    
    
class Secrets:
    def __init__(self):
        self.gemini_api_key = gemini_api_key
        self.gemini_api_url = gemini_api_url
        self.gemini_api_model = gemini_api_model