import React from "react";
import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import axios from "axios";
import App from "../App";

// Mock axios
// 模擬請求
jest.mock("axios");


describe("App Component 測試", () => {
  test("應該顯示標題 '使用者管理系統'", () => {
    render(<App />);
    expect(screen.getByText("使用者管理系統")).toBeInTheDocument();
  });

  test("應該成功載入並顯示使用者列表", async () => {
    // 模擬 API 回應
    const mockUsers = [
      { id: 1, name: "Alice", email: "alice@example.com" },
      { id: 2, name: "Bob", email: "bob@example.com" },
    ];
    axios.get.mockResolvedValue({ data: mockUsers });

    render(<App />);
    
    // 確保資料載入後顯示
    await waitFor(() => {
      expect(screen.getByText("Alice")).toBeInTheDocument();
      expect(screen.getByText("Bob")).toBeInTheDocument();
    });
  });

  test("應該能夠填寫表單並提交", async () => {
    // 模擬 POST 請求
    axios.post.mockResolvedValue({
      data: { message: "User added successfully!" },
    });

    render(<App />);
    
    // 填寫表單
    fireEvent.change(screen.getByPlaceholderText("輸入姓名"), { target: { value: "Charlie" } });
    fireEvent.change(screen.getByPlaceholderText("輸入 Email"), { target: { value: "charlie@example.com" } });

    // 點擊提交按鈕
    fireEvent.click(screen.getByText("新增使用者"));

    // 確保 API 被呼叫
    await waitFor(() => {
      expect(axios.post).toHaveBeenCalledWith(expect.any(String), {
        name: "Charlie",
        email: "charlie@example.com",
      });
    });
  });
});
