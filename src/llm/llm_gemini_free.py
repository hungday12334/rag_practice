from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
load_dotenv()
def get_llm_gemini_free() -> ChatGoogleGenerativeAI:
    return ChatGoogleGenerativeAI(model = "gemini-2.5-flash", google_api_key= os.getenv("API_KEY"))