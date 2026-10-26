from config import DATA_PATH

from loaders.pdf_loader import PDFLoader

from splitter.text_splitter import DocumentSplitter

from utils.document_utils import DocumentProcessor


class DocumentService:

    def __init__(self):

        self.loader = PDFLoader(DATA_PATH)

        self.splitter = DocumentSplitter()

    def get_documents(self):

        documents = self.loader.load_documents()

        chunks = self.splitter.split_documents(documents)

        chunks = DocumentProcessor.process_documents(chunks)

        print(f"Processed Chunks: {len(chunks)}")

        return chunks