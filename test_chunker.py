from utils.parser import PDFParser
from utils.chunker import TextChunker

parser = PDFParser()
docs = parser.load_pdf("data/MEITY part2-Page-24.pdf")

chunker = TextChunker()

chunks = chunker.split_documents(docs)

print("=" * 60)
print("Total Pages :", len(docs))
print("Total Chunks :", len(chunks))
print("=" * 60)

for i, chunk in enumerate(chunks[:5]):

    print(f"\nChunk {i+1}")

    print(chunk.metadata)

    print(chunk.page_content[:])

    print("-"*60)