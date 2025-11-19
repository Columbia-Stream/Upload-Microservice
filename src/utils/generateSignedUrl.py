from google.cloud import storage
from datetime import timedelta
import uuid

def generate_video_id():
    # Generate a Version 4 (random) UUID and return it as a string
    new_uuid = str(uuid.uuid4())
    return new_uuid

def create_gcs_signed_upload_url(
    bucket_name: str, 
    video_id: str = None,
    file_extension: str = ".mp4",
    # mime_type: str,
    expiration_minutes: int = 15
) -> str:
    """
    Generates a v4 signed URL for uploading a raw video file to a GCS bucket.
    
    Args:
        bucket_name: Your Google Cloud Storage bucket name (e.g., 'columbiastream_video_storage').
        video_id: The unique ID generated for the video in Step 2.
        file_extension: The expected extension of the user's file (e.g., .mp4, .mov).
        expiration_minutes: How long the URL is valid for (to limit security risk).

    Returns:
        The secure, time-limited signed URL string.
    """
    storage_client = storage.Client(project="qualified-root-474022-u3")
    
    # 1. Define the exact path (Blob Name) where the raw file will be stored.
    # We use a /raw/ prefix to keep the *original* file separate from the *encoded* files.
    # The file name includes the video_id for easy tracking later.
    blob_name = f"raw/{video_id}/upload_{video_id}{file_extension}"
    raw_gcs_path = f"gs://{bucket_name}/{blob_name}"

    # 2. Get a reference to the specific bucket.
    bucket = storage_client.bucket(bucket_name)
    
    # 3. Get a reference to the specific file path (blob).
    blob = bucket.blob(blob_name)

    # 4. Define the security parameters for the signed URL.
    url = blob.generate_signed_url(
        version="v4", 
        # The URL is valid for 15 minutes. This is a security measure.
        expiration=timedelta(minutes=expiration_minutes), 
        # The HTTP method must be PUT because the client is writing (uploading) the file.
        method="PUT",
        # This is CRITICAL for security: it ensures the client can ONLY upload
        # a file with the specific Content-Type expected (e.g., a video file).
        content_type="video/quicktime" #For testing
        # content_type=mime_type,
    )

    return url, raw_gcs_path

# --- Example Usage (in your Upload Microservice logic) ---
# bucket_name = "columbiastream_video_storage"
# video_id_from_db = 12345
# signed_url = create_gcs_signed_upload_url(bucket_name, video_id_from_db)
# print(f"Frontend should use this URL: {signed_url}")