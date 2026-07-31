from utils.retriever import Retriever
from utils.reranker import Reranker
from utils.llm import LLM

question = input("Question : ")

retriever = Retriever()
retrieved_docs = retriever.retrieve(question)

reranker = Reranker()
top_docs = reranker.rerank(question, retrieved_docs)

llm = LLM()

answer = llm.generate(question, top_docs)

print("\n")
print("=" * 80)
print("FINAL ANSWER")
print("=" * 80)
print(answer)

print("\n")
print("=" * 80)
print("SOURCES")
print("=" * 80)

for i, doc in enumerate(top_docs, start=1):
    print(f"{i}. {doc.metadata['source']} | Page: {doc.metadata['page'] + 1}")