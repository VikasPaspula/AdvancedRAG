import os

from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

from config import GEMINI_MODEL


load_dotenv()


class LLMModel:

    def __init__(self):

        api_key = os.getenv("GOOGLE_API_KEY")

        if not api_key:

            raise ValueError(
                "GOOGLE_API_KEY not found in .env"
            )

        self.llm = ChatGoogleGenerativeAI(

            model=GEMINI_MODEL,

            google_api_key=api_key,

            temperature=0

        )

    def get_llm(self):

        return self.llm