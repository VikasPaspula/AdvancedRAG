from operator import itemgetter

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

from prompts.rag_prompt import RAG_PROMPT


class RAGChain:

    def __init__(self, retriever, llm):

        self.retriever = retriever

        self.llm = llm

    @staticmethod
    def format_docs(documents):

        return "\n\n".join(
            document.page_content
            for document in documents
        )

    def build_chain(self):

        chain = (

            {

                "context":

                    itemgetter("question")

                    | self.retriever

                    | RunnableLambda(self.format_docs),

                "question":

                    itemgetter("question"),

            }

            | RAG_PROMPT

            | self.llm

            | StrOutputParser()

        )

        return chain