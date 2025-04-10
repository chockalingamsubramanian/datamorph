import boto3
import os

def load_data_from_s3(bucket, key, download_path="data/"):
    try:
        os.makedirs(download_path, exist_ok=True)
        file_path = os.path.join(download_path, os.path.basename(key))

        s3 = boto3.client('s3')
        s3.download_file(bucket, key, file_path)

        print(f"📥 Downloaded {key} from S3 bucket '{bucket}' to {file_path}")
        return {"file_path": file_path}

    except Exception as e:
        print(f"[❌] Failed to download from S3: {e}")
        return {"error": str(e)}
