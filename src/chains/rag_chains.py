from langchain_core.documents import Document

from src.embeddings import get_nomic_embed
from src.llm import get_llm_gemini_free
from src.prompts import get_prompt
from src.retrieval import create_retrieval
from src.vectordb import get_qdrant_vector_store

def format_documents(documents: list[Document]) -> str:
    return "\n\n".join(
        f"[Source: {doc.metadata.get('source', 'unknown')}]\n{doc.page_content}"
        for doc in documents
    )


def ask_rag(question: str) -> str:
    embeddings = get_nomic_embed()
    vector_store = get_qdrant_vector_store("EventHub",embeddings)
    retriever = create_retrieval(vector_store, k=5)
    llm = get_llm_gemini_free()
    
    documents = retriever.invoke(question)
    context = format_documents(documents)
    prompt_value = get_prompt(question, context)
    response = llm.invoke(prompt_value)
    return response.content