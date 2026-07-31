from utils.vectorstore import VectorStore
from config import TOP_K


class Retriever:

    def __init__(self):
        self.db = VectorStore().load_vectorstore()

    def retrieve(self, query: str):
        results = self.db.similarity_search(
            query=query,
            k=TOP_K
        )
        return results