from weaviate import WeaviateClient
from weaviate.classes.config import Property, DataType, VectorIndexConfig
import numpy as np

# Connect to Weaviate (local instance)
client = WeaviateClient(
    url="http://localhost:8080",  # Make sure Weaviate is running here
)

# Create the collection if it doesn't exist
if not client.collections.exists("DocumentChunk"):
    client.collections.create(
        name="DocumentChunk",
        properties=[
            Property(name="doc_id", data_type=DataType.TEXT),
            Property(name="chunk_id", data_type=DataType.TEXT),
            Property(name="metadata", data_type=DataType.TEXT),
        ],
        vector_index_config=VectorIndexConfig(dimension=384)  # Set your embedding size here
    )
    print("Created 'DocumentChunk' collection")

# Store an embedding in the collection
def store_embedding(doc_id, chunk_id, vector, metadata):
    collection = client.collections.get("DocumentChunk")
    collection.data.insert(
        properties={
            "doc_id": doc_id,
            "chunk_id": chunk_id,
            "metadata": metadata
        },
        vector=np.array(vector, dtype=np.float32)  # ensure correct type
    )
    print(f"Inserted chunk: {chunk_id} from document: {doc_id}")