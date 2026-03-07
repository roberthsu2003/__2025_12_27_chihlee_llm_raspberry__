FROM python:3.11-slim

WORKDIR /app

# 安裝 mcpo 與 mcp-server-time
RUN pip install --no-cache-dir mcpo mcp-server-time

# 對外開放 8000 埠
EXPOSE 8000

# 啟動 mcpo，並掛載 mcp-server-time
CMD ["mcpo", "--port", "8000", "--", "mcp-server-time", "--local-timezone=Asia/Taipei"]
