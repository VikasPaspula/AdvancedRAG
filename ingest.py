from services.document_service import DocumentService

from models.embeddings import EmbeddingModel

from vectorstore.chroma_store import ChromaVectorStore


def main():

    print("=" * 60)
    print("Starting Document Ingestion")
    print("=" * 60)

    # Load and Process Documents
    chunks = DocumentService().get_documents()

    print("\nSample Metadata")

    print(chunks[0].metadata)

    # Load Embedding Model
    embedding_model = EmbeddingModel().get_embeddings()

    # Create ChromaDB
    ChromaVectorStore(

        embedding_model

    ).create_vector_store(

        chunks

    )

    print("\nIngestion Completed Successfully")


if __name__ == "__main__":

    main()