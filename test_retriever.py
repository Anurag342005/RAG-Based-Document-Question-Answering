from utils.retriever import Retriever

retriever = Retriever()

query = input("Enter your question: ")

results = retriever.retrieve(query)

print("\n" + "=" * 70)
print(f"Retrieved {len(results)} Documents")
print("=" * 70)

for i, doc in enumerate(results, start=1):
    print(f"\nResult {i}")
    print("-" * 70)
    print("Metadata:", doc.metadata)
    print("Content:")
    print(doc.page_content[:])