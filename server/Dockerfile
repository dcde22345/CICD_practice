# 使用python 3.11
FROM python:3.11

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# 複製 Flask 源碼
COPY . .

# 指定 Flask 運行的 Port
EXPOSE 5000

# 啟動 Flask
CMD ["python", "app.py"]