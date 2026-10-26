from langchain_chroma import Chroma

from config import (
    CHROMA_DB_PATH,
    COLLECTION_NAME,
    TOP_K
)


class ChromaRetriever:

    def __init__(self, embedding_model):

        self.vector_store = Chroma(
            persist_directory=str(CHROMA_DB_PATH),
            embedding_function=embedding_model,
            collection_name=COLLECTION_NAME
        )

    def get_retriever(self):

        return self.vector_store.as_retriever(
            search_kwargs={
                "k": TOP_K
            }
        )

    def similarity_search(self, question):

        return self.vector_store.similarity_search(
            question,
            k=TOP_K
        )