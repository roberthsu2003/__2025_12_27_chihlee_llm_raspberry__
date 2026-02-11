FROM python:3.11-slim

WORKDIR /app

# 安裝套件
RUN pip install --no-cache-dir mcpo mcp-server-time

# 開放 8000 port
EXPOSE 8000

# 啟動指令
CMD ["mcpo", "--port", "8000", "--", "mcp-server-time", "--local-timezone=Asia/Taipei"]
