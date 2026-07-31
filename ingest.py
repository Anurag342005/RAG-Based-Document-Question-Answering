from utils.parser import PDFParser
from utils.chunker import TextChunker
from utils.vectorstore import VectorStore

print("=" * 60)
print("Loading PDF...")
print("=" * 60)

parser = PDFParser()
documents = parser.load_pdf("data/MEITY part2-Page-24.pdf")

print(f"Pages Loaded : {len(documents)}")

print("=" * 60)
print("Chunking...")
print("=" * 60)

chunker = TextChunker()
chunks = chunker.split_documents(documents)

print(f"Total Chunks : {len(chunks)}")

print("=" * 60)
print("Creating ChromaDB...")
print("=" * 60)

db = VectorStore()
db.create_vectorstore(chunks)

print("✅ Vector Database Created Successfully")