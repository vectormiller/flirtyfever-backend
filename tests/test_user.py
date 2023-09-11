from fastapi.testclient import TestClient
from src.main import app
from src.settings import settings


def test_getResponse():
    client = TestClient(app)
    response = client.get(f"{settings.MAIN_URL}user/1")
    assert response.status_code == 200
    # If you want to compare response body, use this:
    # assert response.json() == {"id": "1", "lastname": "Miller"}