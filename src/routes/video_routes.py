from fastapi import APIRouter, UploadFile, Form, status
from src.models.video_model import VideoUpdate

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
