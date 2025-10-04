# Upload Video Microservice

This microservice handles **video file uploads** and manages **video metadata** such as course ID, course name, professor name, and video title.  
It is designed using **FastAPI** and follows an **API-first approach** with a Swagger/OpenAPI definition.

---

## API Endpoints

| Endpoint       | Method | Description                            |
| -------------- | ------ | -------------------------------------- |
| `/videos`      | GET    | Get all uploaded videos (returns 501)  |
| `/videos`      | POST   | Upload a new video with metadata (501) |
| `/videos/{id}` | GET    | Get video details by ID (501)          |
| `/videos/{id}` | PUT    | Update video metadata (501)            |
| `/videos/{id}` | DELETE | Delete a video by ID (501)             |

