# Upload Video Microservice
## To Start Service Locally

python3 -m uvicorn main:app --host 0.0.0.0 --port 8001 --reload
gcloud auth application-default login --impersonate-service-account=upload-service@qualified-root-474022-u3.iam.gserviceaccount.com   
<!-- To update cred - gcloud auth login --update-adc -->
python3 -m http.server 3000 to test frontend

./cloud-sql-proxy qualified-root-474022-u3:us-central1:upload-db-cloud-instance --port=3306 For proxy

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

