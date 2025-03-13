# GET /users 應該回傳 200 並且是 list
# POST /users 應該成功新增使用者
import json
import pytest
from app import app

@pytest.fixture
def client():
    """建立測試用的 Flask 客戶端"""
    app.testing = True
    return app.test_client()

def test_get_users(client):
    """測試 GET /users"""
    response = client.get('/users')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)  # 回傳應該是 list

def test_add_user(client):
    """測試 POST /users"""
    new_user = {"name": "Test User", "email": "test@example.com"}
    response = client.post('/users', data=json.dumps(new_user), content_type='application/json')

    assert response.status_code == 201
    assert response.get_json()["message"] == "User added successfully!"
