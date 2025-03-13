# Email 重複 應該回傳 400
# 缺少 name 或 email 應該回傳 400

import json
import pytest
from app import app

@pytest.fixture
def client():
    """建立測試用的 Flask 客戶端"""
    app.testing = True
    return app.test_client()

def test_add_duplicate_user(client):
    """測試當 email 重複時，應該回傳 400"""
    user = {"name": "Test User", "email": "duplicate@example.com"}

    # 第一次新增應該成功
    response = client.post('/users', data=json.dumps(user), content_type='application/json')
    assert response.status_code == 201

    # 第二次新增應該失敗
    response = client.post('/users', data=json.dumps(user), content_type='application/json')
    assert response.status_code == 400  # 應該回傳 400 Bad Request

def test_add_user_missing_field(client):
    """測試當缺少 name 或 email 時，應該回傳 400"""
    response = client.post('/users', data=json.dumps({"name": "No Email"}), content_type='application/json')
    assert response.status_code == 400
