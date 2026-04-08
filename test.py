from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()  # must be FIRST

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
