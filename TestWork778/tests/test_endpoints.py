from fastapi.testclient import TestClient
from datetime import datetime

def test_add_transaction(client):
    response = client.post(
        "/transactions",
        json={
            "transaction_id": "test123",
            "user_id": "user001",
            "amount": 100.0,
            "currency": "USD",
            "timestamp": datetime.now().isoformat()
        },
        headers={"Authorization": "ApiKey your_secret_api_key"}
    )
    assert response.status_code == 200
    assert "message" in response.json()
    assert "task_id" in response.json()

def test_delete_transactions(client):
    response = client.delete(
        "/transactions",
        headers={"Authorization": "ApiKey your_secret_api_key"}
    )
    assert response.status_code == 200
    assert response.json()["message"] == "All transactions deleted"

def test_get_statistics(client):
    # First add some transactions
    for i in range(3):
        client.post(
            "/transactions",
            json={
                "transaction_id": f"test{i}",
                "user_id": "user001",
                "amount": 100.0 * (i + 1),
                "currency": "USD",
                "timestamp": datetime.now().isoformat()
            },
            headers={"Authorization": "ApiKey your_secret_api_key"}
        )
    
    response = client.get(
        "/statistics",
        headers={"Authorization": "ApiKey your_secret_api_key"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["total_transactions"] == 3
    assert len(data["top_transactions"]) <= 3