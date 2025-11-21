from pydantic import BaseModel
from typing import Optional

# Response model for video metadata
class Video(BaseModel):
    id: str
    courseId: str
    courseName: str
    professorName: str
    videoTitle: str
    fileUrl: Optional[str] = None   # link to stored video

# Request model for updating metadata (no file upload here)
class VideoUpdate(BaseModel):
    courseId: Optional[str]
    courseName: Optional[str]
    professorName: Optional[str]
    videoTitle: Optional[str]

class VideoUpload(BaseModel):
    offering_id: int
    prof_uni: str
    videoTitle: str

