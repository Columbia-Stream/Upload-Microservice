import httpx
from src.utils.config import VIDEO_DOMAIN

def send_metadata_to_composite(db_payload):
    try:
        with httpx.Client() as client:
            response = client.post(
                f"{VIDEO_DOMAIN}/videos/metadata",
                json=db_payload,
                timeout=10.0
            )
            print("Metadata stored:", response.status_code)
    except Exception as e:
        print("Error sending metadata:", str(e))
