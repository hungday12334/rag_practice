from langchain_core.vectorstores import VectorStoreRetriever
from langchain_qdrant import QdrantVectorStore

def create_retrieval(vector_store: QdrantVectorStore, k:int =5) -> VectorStoreRetriever:
    return vector_store.as_retriever(search_kwargs = {"k":k})