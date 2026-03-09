"""
直接測試 Filter 邏輯，不需啟動 Open WebUI
"""

from main import Filter

f = Filter()

# 模擬inlet的body
body_inlet = {
    "messages": [
        {"role": "user", "content": "您好,請介紹台灣"}
    ],
    "model": "llama3.1"
}

# 測試 inlet

result = f.inlet(body_inlet, None)
print("inlet 輸出:", result["messages"][-1]["content"])

# 模擬outlet的body(含AI回答)
body_outlet ={
    "messages":[
        {"role": "user", "content": "您好"},
        {"role": "assistant", "content": "你好:有什麼可以幫你的?"},
    ]
}

# 測試outlet
result = f.outlet(body_outlet, None)
print("outlet 輸出:", result["messages"][-1]["content"])