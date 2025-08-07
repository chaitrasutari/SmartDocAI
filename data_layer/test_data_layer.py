from mongodb.mongodb_store import save_document_metadata, get_document
from storage.minio_uploader import upload_file, download_file
from vectordb.weaviate_client import store_embedding
import numpy as np

doc_id = "doc001"
filename = "example.pdf"
file_path = "example.pdf"
key = "uploads/example.pdf"

# Upload to MinIO
minio_url = upload_file(file_path, key)

# Save to MongoDB
summary = "This is a test summary of the document."
save_document_metadata(doc_id, filename, summary, minio_url)

# Store vector
vector = np.random.rand(384).tolist()
metadata = { "section": "intro" }
store_embedding(doc_id, "chunk001", vector, metadata)

# Fetch from MongoDB
result = get_document(doc_id)
print("Retrieved from MongoDB:", result)

# Optionally download the file
# download_file(key, "downloaded_example.pdf")