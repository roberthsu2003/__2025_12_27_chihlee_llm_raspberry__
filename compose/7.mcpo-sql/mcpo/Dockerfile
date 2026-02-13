FROM python:3.11-slim

# 安裝 curl（下載 uv 用）
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# 安裝 uv
RUN curl -Ls https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

# 安裝 mcpo
RUN uv tool install mcpo

# 開放 port（MCPO 對外）
EXPOSE 8000

# 啟動 MCPO，並透過 uvx 啟動 postgres-mcp
CMD ["mcpo", \
  "--port", "8000", \
  "--", \
  "uvx", "postgres-mcp"]
