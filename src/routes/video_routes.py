from fastapi import APIRouter, UploadFile, Form, status, HTTPException
from src.models.video_model import VideoUpdate
from src.utils.generateSignedUrl import create_gcs_signed_upload_url, generate_video_id

router = APIRouter()

# GET /videos
@router.get("/", status_code=status.HTTP_501_NOT_IMPLEMENTED, responses={501: {"description": "NOT IMPLEMENTED"}})
async def get_videos():
    return {"detail": "NOT IMPLEMENTED"}

# POST /videos
@router.post("/", status_code=status.HTTP_501_NOT_IMPLEMENTED, responses={501: {"description": "NOT IMPLEMENTED"}})
async def upload_video(
    file: UploadFile,
    courseId: str = Form(...),
    courseName: str = Form(...),
    professorName: str = Form(...),
    videoTitle: str = Form(...)
):
    return {"detail": "NOT IMPLEMENTED"}

# GET /videos/{id}
@router.get("/{id}", status_code=status.HTTP_501_NOT_IMPLEMENTED, responses={501: {"description": "NOT IMPLEMENTED"}})
async def get_video(id: str):
    return {"detail": "NOT IMPLEMENTED"}

# PUT /videos/{id}
@router.put("/{id}", status_code=status.HTTP_501_NOT_IMPLEMENTED, responses={501: {"description": "NOT IMPLEMENTED"}})
async def update_video(id: str):
    return {"detail": "NOT IMPLEMENTED"}

# DELETE /videos/{id}
@router.delete("/{id}", status_code=status.HTTP_501_NOT_IMPLEMENTED, responses={501: {"description": "NOT IMPLEMENTED"}})
async def delete_video(id: str):
    return {"detail": "NOT IMPLEMENTED"}

# To start upload
@router.post("/start_upload", status_code=status.HTTP_200_OK, responses={501: {"description": "NOT IMPLEMENTED"}, 200: {"description": "Upload Started"}})
async def upload_video(
    # file: UploadFile,
    courseId: str = Form(...),
    courseName: str = Form(...),
    emailId: str = Form(...),
    videoTitle: str = Form(...)
):
    try:
        video_id = generate_video_id()
        signed_url = create_gcs_signed_upload_url(
            bucket_name="columbiastream_video_store",
            file_extension='.mp4',
        )
        print("\n✅ SIGNED URL GENERATED SUCCESSFULLY:")
        print(signed_url)
        
        return {"detail": "NOT IMPLEMENTED 1", courseId: courseId}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))