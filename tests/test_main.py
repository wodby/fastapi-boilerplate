from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_index():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Your FastAPI app is running"
    assert response.json()["docs"] == "/docs"


def test_docs():
    assert client.get("/docs").status_code == 200

    schema = client.get("/openapi.json").json()
    assert "/api/greetings" in schema["paths"]
    assert "/healthz" not in schema["paths"]


def test_status():
    response = client.get("/api/status")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_greeting():
    response = client.post(
        "/api/greetings",
        json={"name": "Ada", "enthusiastic": True},
    )

    assert response.status_code == 201
    assert response.json() == {
        "message": "Hello, Ada!",
        "framework": "FastAPI",
    }


def test_greeting_validation():
    response = client.post("/api/greetings", json={"name": "   "})

    assert response.status_code == 422


def test_method_not_allowed():
    response = client.post("/")

    assert response.status_code == 405


def test_healthz():
    response = client.get("/healthz")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
