from langchain_chroma import Chroma

from config import CHROMA_DB_PATH
from config import COLLECTION_NAME


class ChromaVectorStore:

    def __init__(self, embedding_model):

        self.embedding_model = embedding_model

    def create_vector_store(self, chunks):

        vector_store = Chroma.from_documents(

            documents=chunks,

            embedding=self.embedding_model,

            persist_directory=str(CHROMA_DB_PATH),

            collection_name=COLLECTION_NAME

        )

        print("=" * 60)
        print("ChromaDB Created Successfully")
        print(f"Stored {len(chunks)} Chunks")
        print("=" * 60)

        return vector_store