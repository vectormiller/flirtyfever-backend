from fastapi.testclient import TestClient
from flirtyfever_backend.main import app
from flirtyfever_backend.settings import settings


def test_getResponse():
    client = TestClient(app)
    response = client.get(f"{settings.MAIN_URL}user/1")
    assert response.status_code == 200
    # If you want to compare response body, use this:
    # assert response.json() == {"id": "1", "lastname": "Miller"}