from fastapi import FastAPI
from src.routes import video_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Upload Video Microservice",
    version="1.0.0",
    description="Handles file uploads and video metadata"
)

# Remove this after testing as this won't be called directly from frontend.
origins = [
    # IMPORTANT: Replace this with the exact URL of your frontend
    "http://localhost:3000", 
    "http://127.0.0.1:3000",
    
    # If using your VM's IP for Postman/Testing (optional, but good for local checks)
    
    # You can add the production domain of your frontend here later (e.g., "https://my-frontend.com")
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,              # Specify allowed origins
    allow_credentials=True,             # Allow cookies/authorization headers
    allow_methods=["*"],                # Allow all methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],                # Allow all headers (Content-Type, Authorization, etc.)
)

# include routes
app.include_router(video_routes.router, prefix="/videos", tags=["Videos"])

# root health check
@app.get("/")
def read_root():
    return {"message": "Upload Video Microservice is running"}
