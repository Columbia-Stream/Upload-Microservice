from fastapi import APIRouter, UploadFile, Form, status, HTTPException
from src.models.video_model import VideoUpdate, VideoUpload
from src.utils.generateSignedUrl import create_gcs_signed_upload_url, generate_video_id
import httpx
from src.utils.config import VIDEO_DOMAIN
import threading
from src.utils.metadata_tasks import send_metadata_to_composite

router = APIRouter()



# To start upload
@router.post("/start_upload", status_code=status.HTTP_202_ACCEPTED, responses={202: {"description": "Upload Initiated"}})
async def upload_video(
    VideoUploadPayload: VideoUpload
):
    try:
        offering_id = VideoUploadPayload.offering_id
        prof_uni = VideoUploadPayload.prof_uni
        videoTitle = VideoUploadPayload.videoTitle
        video_id = generate_video_id()
        url, path = create_gcs_signed_upload_url(
            bucket_name="columbiastream_video_store",
            file_extension='.mp4',
            video_id=video_id
        )
        print("\n✅ SIGNED URL GENERATED SUCCESSFULLY:")
        print(url, path)
        db_payload = {
            "video_id": video_id,
            "gcs_path": path,
            "offering_id": offering_id,
            "prof_uni": prof_uni,
            "title": videoTitle
        }
        # with httpx.Client() as client:
        #     print(f"Calling Composite Service at: {VIDEO_DOMAIN}")
        #     response = client.post(f"{VIDEO_DOMAIN}/videos/metadata", json=db_payload, timeout=10.0)
            
        #     # Check if the Composite Service successfully inserted the data
        #     if response.status_code != 200:
        #         raise HTTPException(
        #             status_code=502, # Bad Gateway
        #             detail=f"Failed to store metadata: {response.text}"
        #         )
        t = threading.Thread(
            target=send_metadata_to_composite,
            args=(db_payload,),
            daemon=True
        )
        t.start()
        
        return {"detail": "Success", "signed_url": url, "video_id": video_id}
    except httpx.ConnectError:
        raise HTTPException(
            status_code=503, # Service Unavailable
            detail=f"Cannot connect to Composite Service at {VIDEO_DOMAIN}."
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# To get offerings
@router.post("/offer", status_code=status.HTTP_200_OK, responses={200: {"description": "Offerings Retrieved"}})
async def get_offerings():
    try:
        
        with httpx.Client() as client:
            print(f"Calling Composite Service at: {VIDEO_DOMAIN}")
            response = client.post(f"{VIDEO_DOMAIN}/videos/offer", timeout=10.0)
            
            # Check if the Composite Service successfully inserted the data
            if response.status_code != 200:
                raise HTTPException(
                    status_code=502, # Bad Gateway
                    detail=f"Failed to fetch offerings: {response.text}"
                )
        
        
        return response.json()
    except httpx.ConnectError:
        raise HTTPException(
            status_code=503, # Service Unavailable
            detail=f"Cannot connect to Composite Service at {VIDEO_DOMAIN}."
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# To get courses
@router.post("/courses", status_code=status.HTTP_200_OK, responses={200: {"description": "Courses Retrieved"}})
async def get_courses():
    try:
        
        with httpx.Client() as client:
            print(f"Calling Composite Service at: {VIDEO_DOMAIN}")
            response = client.post(f"{VIDEO_DOMAIN}/videos/courses", timeout=10.0)
            
            # Check if the Composite Service successfully inserted the data
            print(f"DEBUG: Response status code: {response}")
            if response.status_code != 200:
                raise HTTPException(
                    status_code=502, # Bad Gateway
                    detail=f"Failed to fetch courses: {response.text}"
                )
        
        
        return response.json()
    except httpx.ConnectError:
        raise HTTPException(
            status_code=503, # Service Unavailable
            detail=f"Cannot connect to Composite Service at {VIDEO_DOMAIN}."
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/prof_offer/{prof_uni}", status_code=status.HTTP_200_OK, responses={200: {"description": "Prof Offerings Retrieved"}})
async def get_prof_offerings(prof_uni: str):
    try:
        
        with httpx.Client() as client:
            print(f"Calling Composite Service at: {VIDEO_DOMAIN}")
            response = client.post(f"{VIDEO_DOMAIN}/videos/prof_offer/{prof_uni}", timeout=10.0)
            
            # Check if the Composite Service successfully inserted the data
            print(f"DEBUG: Response status code: {response}")
            if response.status_code != 200:
                raise HTTPException(
                    status_code=502, # Bad Gateway
                    detail=f"Failed to fetch prof_offerings: {response.text}"
                )
        
        
        return response.json()
    except httpx.ConnectError:
        raise HTTPException(
            status_code=503, # Service Unavailable
            detail=f"Cannot connect to Composite Service at {VIDEO_DOMAIN}."
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
