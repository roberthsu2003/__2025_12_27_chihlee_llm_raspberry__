"""
title: Debug Filter
author: test
version: 0.1
"""

from typing import Optional


class Filter:
    def inlet(self, body: dict, __user__: Optional[dict] = None) -> dict:
        print("=== FILTER INLET CALLED ===")
        print("User:", __user__)
        print("Body keys:", body.keys())
        print("==========================")
        return body

    def outlet(self, body: dict, __user__: Optional[dict] = None) -> dict:
        print("=== FILTER OUTLET CALLED ===")
        print("User:", __user__)
        print("Response keys:", body.keys())
        print("===========================")
        return body
