from sentence_transformers import CrossEncoder
from config import RERANKER_MODEL, FINAL_K


class Reranker:

    def __init__(self):
        self.model = CrossEncoder(RERANKER_MODEL)

    def rerank(self, query, documents):

        pairs = [
            (query, doc.page_content)
            for doc in documents
        ]

        scores = self.model.predict(pairs)

        ranked = list(zip(documents, scores))

        ranked.sort(
            key=lambda x: x[1],
            reverse=True
        )

        top_docs = [
            doc
            for doc, score in ranked[:FINAL_K]
        ]

        return top_docs