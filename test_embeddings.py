from utils.embeddings import EmbeddingModel

embedding = EmbeddingModel().get_embedding_model()

vector = embedding.embed_query("What is Artificial Intelligence?")

print("=" * 60)
print("Embedding Dimension :", len(vector))
print("=" * 60)
print(vector[:])