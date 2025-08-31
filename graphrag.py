import os
import logging
import sys

from dotenv import load_dotenv
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.core import Settings
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding
from google.genai.types import EmbedContentConfig


load_dotenv()
logging.basicConfig(
    stream=sys.stdout, level=logging.INFO
)


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

embed_model = GoogleGenAIEmbedding(
    model_name="text-embedding-004",
    embed_batch_size=100
)

Settings.llm = GoogleGenAI(
    model="gemini-2.0-flash",
)
Settings.embed_model = embed_model
Settings.chunk_size = 512

space_name = "llamaindex"
edge_types, rel_prop_names = ["relationship"], [
    "relationship"
]
tags = ["entity"]