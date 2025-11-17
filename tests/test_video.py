import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_videos():
    response = client.get("/videos")
    assert response.status_code == 501
    assert response.json() == {"detail": "NOT IMPLEMENTED"}

def test_post_video():
    # simulate file upload with form data
    response = client.post(
        "/videos",
        files={"file": ("test.mp4", b"dummy content")},
        data={
            "courseId": "CS101",
            "courseName": "Intro to CS",
            "professorName": "Dr. Smith",
            "videoTitle": "Lecture 1"
        }
    )
    assert response.status_code == 501
    assert response.json() == {"detail": "NOT IMPLEMENTED"}

def test_get_video_by_id():
    response = client.get("/videos/123")
    assert response.status_code == 501
    assert response.json() == {"detail": "NOT IMPLEMENTED"}

def test_put_video():
    response = client.put("/videos/123")
    assert response.status_code == 501

def test_delete_video():
    response = client.delete("/videos/123")
    assert response.status_code == 501
    assert response.json() == {"detail": "NOT IMPLEMENTED"}
