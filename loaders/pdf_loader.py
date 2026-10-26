from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader


class PDFLoader:

    def __init__(self, data_path: Path):
        self.data_path = data_path

    def load_documents(self):

        documents = []

        pdf_files = list(self.data_path.glob("*.pdf"))

        if not pdf_files:
            raise FileNotFoundError(
                f"No PDF files found in {self.data_path}"
            )

        print("=" * 60)
        print("Loading PDF Documents")
        print("=" * 60)

        for pdf in pdf_files:

            print(f"Loading: {pdf.name}")

            loader = PyPDFLoader(str(pdf))

            documents.extend(loader.load())

        print(f"\nTotal Pages Loaded: {len(documents)}")

        return documents