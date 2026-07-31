import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

PDF_FOLDER = "data"

CHROMA_PATH = "chroma_db"

EMBEDDING_MODEL = "nomic-ai/nomic-embed-text-v1.5"

RERANKER_MODEL = "cross-encoder/ms-marco-MiniLM-L-6-v2"

LLM_MODEL = "openai/gpt-oss-120b"

CHUNK_SIZE = 800

CHUNK_OVERLAP = 100

TOP_K = 10

FINAL_K = 3