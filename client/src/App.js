import React, { useState, useEffect } from "react";
import axios from "axios";
import { Container, Card, Button, Form, Row, Col } from "react-bootstrap";

const API_URL = "http://127.0.0.1:5000/users"; // Flask API 端點

function App() {
  const [users, setUsers] = useState([]);
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");

  // 取得所有使用者
  useEffect(() => {
    fetchUsers();
  }, []);

  const fetchUsers = async () => {
    try {
      const response = await axios.get(API_URL);
      setUsers(response.data);
    } catch (error) {
      console.error("Error fetching users:", error);
    }
  };

  // 新增使用者
  const handleAddUser = async (e) => {
    e.preventDefault();
    try {
      await axios.post(API_URL, { name, email });
      setName("");
      setEmail("");
      fetchUsers(); // 重新載入使用者列表
    } catch (error) {
      console.error("Error adding user:", error);
    }
  };

  return (
    <Container className="mt-5">
      <h2 className="text-center mb-4">使用者管理系統</h2>

      {/* 使用者列表 */}
      <Row className="mb-4">
        {users.map((user) => (
          <Col md={4} key={user.id} className="mb-3">
            <Card>
              <Card.Body>
                <Card.Title>{user.name}</Card.Title>
                <Card.Text>{user.email}</Card.Text>
              </Card.Body>
            </Card>
          </Col>
        ))}
      </Row>

      {/* 新增使用者表單 */}
      <Card className="p-4">
        <h4 className="text-center mb-3">新增使用者</h4>
        <Form onSubmit={handleAddUser}>
          <Form.Group className="mb-3">
            <Form.Label>姓名</Form.Label>
            <Form.Control
              type="text"
              placeholder="輸入姓名"
              value={name}
              onChange={(e) => setName(e.target.value)}
              required
            />
          </Form.Group>

          <Form.Group className="mb-3">
            <Form.Label>Email</Form.Label>
            <Form.Control
              type="email"
              placeholder="輸入 Email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </Form.Group>

          <Button variant="primary" type="submit" className="w-100">
            新增使用者
          </Button>
        </Form>
      </Card>
    </Container>
  );
}

export default App;