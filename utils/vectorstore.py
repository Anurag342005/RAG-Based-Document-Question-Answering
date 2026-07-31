from langchain_chroma import Chroma

from config import CHROMA_PATH
from utils.embeddings import EmbeddingModel


class VectorStore:

    def __init__(self):
        self.embedding = EmbeddingModel().get_embedding_model()

    def create_vectorstore(self, chunks):

        db = Chroma.from_documents(
            documents=chunks,
            embedding=self.embedding,
            persist_directory=CHROMA_PATH
        )

        return db

    def load_vectorstore(self):

        db = Chroma(
            persist_directory=CHROMA_PATH,
            embedding_function=self.embedding
        )

        return db