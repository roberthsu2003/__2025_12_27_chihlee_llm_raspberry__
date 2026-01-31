# __2025_12_27_chihlee_llm_raspberry__
2025_12_27 致理_LLM_Raspberry_上課用

## 上課網址
https://meet.google.com/quo-vmmd-erp


## n8n_for_raspberry_with_ngrok

```
docker run -d \
  --name n8n \
  --network=host \
  -e N8N_HOST=superinnocent-hillary-unwholesome.ngrok-free.dev \
  -e N8N_PROTOCOL=https \
  -e N8N_PORT=5678 \
  -e N8N_EDITOR_BASE_URL=https://superinnocent-hillary-unwholesome.ngrok-free.dev \
  -e WEBHOOK_URL=https://superinnocent-hillary-unwholesome.ngrok-free.dev \
  -e GENERIC_TIMEZONE=Asia/Taipei \
  -v n8n_data:/home/node/.n8n \
  docker.n8n.io/n8nio/n8n
```
