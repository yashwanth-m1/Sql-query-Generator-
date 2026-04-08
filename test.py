from dotenv import load_dotenv
import os
from google import genai

load_dotenv()  # must be FIRST

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
