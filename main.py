# Điểm khởi động.
from src.ingestion import load_txt_file
def main():
    file_path = "document/EventHubs.txt"  # Đường dẫn đến file .txt của bạn
    try:
        print(f"Loading documents from: {file_path}")
        documents  = load_txt_file(file_path, encoding="utf-8", field="business rule")
        print(f"Successfully loaded {len(documents)} documents.")
        if documents:
            print("Sample document content:")
            print(documents[0].page_content)
            print("Sample document metadata:")
            print(documents[0].metadata)
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    main()