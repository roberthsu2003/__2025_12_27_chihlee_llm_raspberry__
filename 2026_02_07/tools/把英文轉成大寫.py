"""
title: 工具名稱
author: 作者名字
version: 1.0
description: 這個工具在做什麼
"""

from pydantic import BaseModel, Field


class Tools:
    class Input(BaseModel):
        text: str = Field(description="使用者輸入的英文文字")

    def my_tool1(self, text: str) -> str:
        """
        將輸入文字轉為大寫
        """
        return text.upper()
