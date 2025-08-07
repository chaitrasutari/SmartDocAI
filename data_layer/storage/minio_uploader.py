import boto3
from botocore.exceptions import NoCredentialsError
from config.config import MINIO_ENDPOINT, MINIO_ACCESS_KEY, MINIO_SECRET_KEY, MINIO_BUCKET

s3 = boto3.client(
    "s3",
    aws_access_key_id=MINIO_ACCESS_KEY,
    aws_secret_access_key=MINIO_SECRET_KEY,
    endpoint_url=MINIO_ENDPOINT,
    region_name="us-east-1"
)

def upload_file(file_path, key):
    try:
        s3.upload_file(file_path, MINIO_BUCKET, key)
        return f"{MINIO_ENDPOINT}/{MINIO_BUCKET}/{key}"
    except NoCredentialsError:
        raise Exception("MinIO credentials not found")

def download_file(key, download_path):
    try:
        s3.download_file(MINIO_BUCKET, key, download_path)
        print(f"Downloaded {key} to {download_path}")
    except NoCredentialsError:
        raise Exception("MinIO credentials not found")