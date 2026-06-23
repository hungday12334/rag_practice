from langchain_ollama.embeddings import OllamaEmbeddings
from dotenv import load_dotenv
import os
load_dotenv()
def get_nomic_embed():
    """
    Returns an instance of OllamaEmbeddings for Nomic embeddings.
    """
    return OllamaEmbeddings(model="nomic-embed-text", base_url=os.getenv("OLLAMA_HOST"))