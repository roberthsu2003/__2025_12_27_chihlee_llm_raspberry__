FROM python:3.11-slim

WORKDIR /app

# 安裝 mcpo 與 mcp-server-time
RUN pip install --no-cache-dir mcpo mcp-server-time

EXPOSE 8000

CMD ["mcpo", "--port", "8000", "--", "mcp-server-time", "--local-timezone=Asia/Taipei"]
