import os
import logging
import sys

from dotenv import load_dotenv
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.core import Settings


load_dotenv()
logging.basicConfig(
    stream=sys.stdout, level=logging.INFO
)


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

llm = GoogleGenAI(
    model="gemini-2.0-flash",
)

resp = llm.complete("Who is Paul Graham?")
print(resp)