from pymongo import MongoClient

def save_document_metadata(document):
    with MongoClient("mongodb://localhost:27017/") as client:
        db = client["smartdoc"]
        collection = db["documents"]
        result = collection.insert_one(document)
        print(f"Inserted document with ID: {result.inserted_id}")

def get_document(document_id):
    from bson.objectid import ObjectId
    with MongoClient("mongodb://localhost:27017/") as client:
        db = client["smartdoc"]
        collection = db["documents"]
        document = collection.find_one({"_id": ObjectId(document_id)})
        return document