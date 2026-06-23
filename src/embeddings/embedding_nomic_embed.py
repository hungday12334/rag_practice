from langchain_ollama.embeddings import OllamaEmbeddings

def get_nomic_embed():
    """
    Returns an instance of OllamaEmbeddings for Nomic embeddings.
    """
    return OllamaEmbeddings(model="nomic-embed-text")