from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def chunk_doc(doc:list[Document], chunk_size: int = 250, chunk_overlap: int = 50) -> list[Document]:
    """
    Chunks the input document into smaller pieces using RecursiveCharacterTextSplitter.

    Args:
        doc (list[Document]): The input documents to be chunked.
        chunk_size (int): The maximum size of each chunk. Default is 250 characters.
        chunk_overlap (int): The number of characters to overlap between chunks. Default is 50 characters.

    Returns:
        list[Document]: A list of chunked documents.
    """
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    
    return text_splitter.split_documents(doc)