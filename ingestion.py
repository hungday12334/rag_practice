# Điểm khởi động.
from langchain_core.documents import Document
from src.chunking import chunk_doc
from src.ingestion import load_txt_file
from src.embeddings import get_nomic_embed
from src.vectordb import create_qdrant_vector_store, get_qdrant_vector_store
from src.prompts import get_prompt
from src.retrieval import create_retrieval
from src.llm import get_llm_gemini_free
def print_document_info(documents: list[Document]):
    """
    Prints the content and metadata of the first document in the list.

    Args:
        documents (list[Document]): A list of Document objects.
    """
    for i, doc in enumerate(documents):
        print(f"Document {i + 1}:")
        print(f"Content: {doc.page_content}")
        print(f"Metadata: {doc.metadata}")
        print("-" * 40)  # Separator for better readability
def main():
    file_path = "document/EventHub.txt"  # Đường dẫn đến file .txt của bạn
    try:
        print(f"Loading documents from: {file_path}")
        documents  = load_txt_file(file_path, encoding="utf-8", field="business rule")
        print(f"Successfully loaded {len(documents)} documents.")
        if documents:
            print("Sample document content:")
            print(documents[0].page_content)
            print("Sample document metadata:")
            print(documents[0].metadata)

        print("Chunking documents...")
        chunked_documents = chunk_doc(documents, chunk_size=250, chunk_overlap=50)
        print(f"Successfully chunked into {len(chunked_documents)} chunks.")
        # print_document_info(chunked_documents)


        print("Starting embedding process...")
        embeddings = get_nomic_embed()

        print("Creating Qdrant vector store...")
        vector_store = create_qdrant_vector_store(chunked_documents, embeddings, collection_name="EventHub")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    main()