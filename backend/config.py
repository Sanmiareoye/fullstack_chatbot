from dotenv import load_dotenv
import openai
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise Exception("OPENAI_API_KEY not found in enviroment variables")

openai.api_key = OPENAI_API_KEY
client = openai