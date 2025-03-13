# 測試 MySQL 連線
# 測試 資料表是否建立

import pymysql
import pytest
from app import get_db_connection, create_table

def test_db_connection():
    """測試 MySQL 是否可以成功連線"""
    connection = None
    try:
        connection = get_db_connection()
        assert connection is not None  # 連線應該成功
    except pymysql.MySQLError as e:
        pytest.fail(f"Database connection failed: {e}")
    finally:
        if connection:
            connection.close()

def test_create_table():
    """測試 `users` 資料表是否建立"""
    create_table()
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SHOW TABLES LIKE 'users';")
        result = cursor.fetchone()
    connection.close()
    
    assert result is not None  # `users` 資料表應該存在
