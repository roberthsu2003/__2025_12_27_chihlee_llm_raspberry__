"""
title: 最簡單的架構
author: 徐國堂
version: 1.0
description: 這是一般的資料
requirements: requests, pydantic
"""

from typing import Optional
import requests
import logging
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class Filter:
    def inlet(self, body: dict, __user__: dict | None = None) -> dict:
        user_message = body["messages"][-1]["content"]
        logger.info(f"[Filter] 使用者輸入: {user_message}")
        logger.debug(f"[Filter] body keys:{body.keys()}")
        # ...
        return body

    def outlet(self, body: dict, __user__: dict | None = None) -> dict:
        assistant_message = body["messages"][-1]["content"]
        print(f"[Filter Debug] AI 回覆: {assistant_message}")  # 會出現在 Open WebUI 的 log
        # ...
        return body


