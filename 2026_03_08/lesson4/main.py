"""
title: 最簡單的架構
author: 徐國堂
version: 1.0
description: 這是一般的資料
requirements: requests, pydantic, google-genai
"""

from typing import Optional
from pydantic import BaseModel, Field
from google import genai
from google.genai import types

client = genai.Client() # 這裡會自動從環境變數 GOOGLE_API_KEY 讀取 API Key


class Filter:
    def inlet(self, body: dict, __user__: dict | None = None) -> dict:
        user_message = body["messages"][-1]["content"]
        print(f"[Filter] 使用者輸入: {user_message}")
        response = client.models.generate_content(
        model="gemini-3-flash-preview",
        config=types.GenerateContentConfig(
                system_instruction="請把輸入的繁體中文,轉換為英文"),
                contents=user_message)
        # 請將response.text的內容加入至body內
        body["messages"][-1]["content"] = response.text        
        return body

    def outlet(self, body: dict, __user__: dict | None = None) -> dict:
        assistant_message = body["messages"][-1]["content"]
        print(f"[Filter Debug] AI 回覆: {assistant_message}")  # 會出現在 Open WebUI 的 log
        # ...
        return body


