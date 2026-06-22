import os
from typing import List
from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document
def load_txt_file(file_path: str, encoding: str = "utf-8", field: str = "") -> List[Document]:
    """
    Load a text file and return its content as a list of documents.

    Args:
        file_path (str): The path to the text file.
        encoding (str): The encoding of the text file.
    """
    if (not os.path.isfile(file_path)) or (not file_path.endswith('.txt')):
        raise FileNotFoundError(f"Invalid file path: {file_path}. Please provide a valid .txt file.")
    try:
        loader = TextLoader(file_path, encoding=encoding)
        documents = loader.load()
        print(f"Loaded {len(documents)} documents from {file_path}")
        print("Dữ liệu được nhập vào là:")
        for doc in documents:
            print(doc.page_content)
        print("Update thêm trường dữ liệu metadata cho các document")
        for doc in documents:
            doc.metadata["field"] = field
            print(f"Document metadata updated: {doc.metadata}")
        return documents
    except Exception as e:
        print(f"Error loading text file: {e}")
        raise RuntimeError(f"Failed to load text file: {e}")
    
