from langchain_qdrant import QdrantVectorStore
import os
from langchain_core.documents import Document
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file
def create_qdrant_vector_store(documents: list[Document], embeddings, collection_name:str) -> QdrantVectorStore:
    """
    Creates a Qdrant vector store from a list of documents.

    Args:
        documents (list[Document]): A list of Document objects to be stored.
        embeddings: The embedding model to be used for vectorization.
        collection_name (str): The name of the Qdrant collection.

    Returns:
        QdrantVectorStore: An instance of QdrantVectorStore containing the documents.
    """
    vector_store =  QdrantVectorStore.from_documents(documents, embeddings, collection_name=collection_name, url = os.getenv("QDRANT_HOST"))