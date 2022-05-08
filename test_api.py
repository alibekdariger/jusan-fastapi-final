from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_sum_to_n():
    response = client.get("/sum1n/{number}")
    assert response.status_code == 202
    assert response.json() == {"result": sum}

def test_fibo():
    response = client.get("/fibo")
    assert response.status_code == 204
    assert response.json() == {"result": n2}

def test_reverse():
    response = client.post("/reverse")
    assert response.status_code == 208
    assert response.json() == {"result": word[:: -1]}




