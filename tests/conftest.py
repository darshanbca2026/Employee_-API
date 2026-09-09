from database import SessionLocal
import crud, schemas
from fastapi.testclient import TestClient
from main import app
import model
import pytest
@pytest.fixture
def client():
    return TestClient(app)
@pytest.fixture
def token(client):

    response = client.post(
        "/login",
        data={
            "username": "darshan",
            "password": "1qaz2wsx"
        }
    )

    return response.json()["access_token"]
@pytest.fixture(autouse=True)
def setup_test_user():
    db = SessionLocal()
    existing = db.query(model.User).filter(model.User.username == "darshan").first()
    if not existing:
        crud.create_user(db, schemas.UserCreate(username="darshan", password="1qaz2wsx"))
    db.close()
    yield