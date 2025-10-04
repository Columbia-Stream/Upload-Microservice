from fastapi import FastAPI
from src.routes import video_routes

app = FastAPI(
    title="Upload Video Microservice",
    version="1.0.0",
    description="Handles file uploads and video metadata"
)

# include routes
app.include_router(video_routes.router, prefix="/videos", tags=["Videos"])

# root health check
@app.get("/")
def read_root():
    return {"message": "Upload Video Microservice is running"}
