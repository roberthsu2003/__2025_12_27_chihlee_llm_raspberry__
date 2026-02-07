"""
title: Debug Filter
author: test
version: 0.1
"""

from typing import Optional


class Filter:
    def inlet(self, body: dict, __user__: Optional[dict] = None) -> dict:
        print("=== 使用者輸入 ===")
        print("User:", __user__)
        print("Body keys:", body.keys())
        print("==========================")
        return body

    def outlet(self, body: dict, __user__: Optional[dict] = None) -> dict:
        print("=== 模型輸出 ===")
        print("User:", __user__)
        print("Response keys:", body.keys())
        print("===========================")
        return body
