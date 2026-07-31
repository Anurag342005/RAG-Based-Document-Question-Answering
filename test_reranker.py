from utils.retriever import Retriever
from utils.reranker import Reranker

query = input("Question : ")

retriever = Retriever()
docs = retriever.retrieve(query)

print(f"\nRetrieved : {len(docs)} documents")

reranker = Reranker()

top_docs = reranker.rerank(query, docs)

print("\nTop Documents After Reranking\n")

for i, doc in enumerate(top_docs, start=1):

    print("=" * 70)
    print(f"Top {i}")
    print(doc.metadata)
    print(doc.page_content[:])