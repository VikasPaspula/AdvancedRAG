from pathlib import Path

from langchain_core.documents import Document


class DocumentProcessor:

    @staticmethod
    def process_documents(documents):

        processed_documents = []

        for index, document in enumerate(documents):

            metadata = {

                "source": Path(
                    document.metadata.get(
                        "source",
                        ""
                    )
                ).name,

                "page": document.metadata.get(
                    "page",
                    0
                ),

                "chunk_id": index

            }

            processed_documents.append(

                Document(

                    page_content=document.page_content,

                    metadata=metadata

                )

            )

        return processed_documents