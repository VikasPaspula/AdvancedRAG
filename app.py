# from models.embeddings import EmbeddingModel
# from models.llm import LLMModel

# from retriever.chroma_retriever import ChromaRetriever

# from chains.rag_chain import RAGChain


# def main():

#     print("=" * 70)
#     print("Advanced RAG System")
#     print("=" * 70)

#     # Load Embedding Model
#     embedding_model = EmbeddingModel().get_embeddings()

#     # Load Gemini
#     llm = LLMModel().get_llm()

#     # Load Retriever
#     retriever = ChromaRetriever(
#         embedding_model
#     ).get_retriever()

#     # Build Chain
#     rag_chain = RAGChain(
#         retriever,
#         llm
#     ).build_chain()

#     while True:

#         question = input("\nAsk a Question (type 'exit' to quit): ")

#         if question.lower() == "exit":
#             print("\nThank you!")
#             break

#         print("\nGenerating Answer...\n")

#         answer = rag_chain.invoke(
#             {
#                 "question": question
#             }
#         )

#         print("=" * 70)
#         print(answer)
#         print("=" * 70)


# if __name__ == "__main__":
#     main()

from models.embeddings import EmbeddingModel
from models.llm import LLMModel

from retriever.chroma_retriever import ChromaRetriever
from chains.rag_chain import RAGChain


def main():

    print("=" * 70)
    print("Advanced RAG System")
    print("=" * 70)

    embedding_model = EmbeddingModel().get_embeddings()

    llm = LLMModel().get_llm()

    chroma = ChromaRetriever(embedding_model)

    retriever = chroma.get_retriever()

    rag_chain = RAGChain(
        retriever,
        llm
    ).build_chain()

    while True:

        question = input("\nAsk a Question (type 'exit' to quit): ")

        if question.lower() == "exit":
            break

        # Retrieve documents
        docs = chroma.similarity_search(question)

        print("\nRetrieved Chunks")
        print("=" * 70)

        for i, doc in enumerate(docs, start=1):

            print(f"\nChunk {i}")

            print(f"Source : {doc.metadata['source']}")

            print(f"Page   : {doc.metadata['page']}")

            print("-" * 70)

        answer = rag_chain.invoke(
            {
                "question": question
            }
        )

        print("\nAnswer")
        print("=" * 70)

        print(answer)

        print("=" * 70)


if __name__ == "__main__":
    main()