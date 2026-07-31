from utils.parser import PDFParser

parser = PDFParser()

docs = parser.load_pdf("data/MEITY part2-Page-24.pdf")

print("=" * 60)

print("Total Pages :", len(docs))

print("=" * 60)

for i, doc in enumerate(docs):

    print(f"\nPage {i+1}")

    print(doc.metadata)

    print(doc.page_content[:])

    print("-" * 50)