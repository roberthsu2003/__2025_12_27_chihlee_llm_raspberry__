"""
title: 範例濾鏡
author: open-webui
author_url: https://github.com/open-webui
funding_url: https://github.com/open-webui
version: 0.1
"""

from typing import Optional


class Filter:
    class Valves:
        """系統層級的設定閥門"""
        def __init__(self):
            self.priority = 0  # 濾鏡操作的優先級別
            self.max_turns = 8  # 使用者允許的最大對話輪數

    class UserValves:
        """使用者層級的設定閥門"""
        def __init__(self):
            self.max_turns = 4  # 使用者允許的最大對話輪數

    def __init__(self):
        """初始化濾鏡實例"""
        # 自訂檔案處理邏輯的標誌。此旗標幫助解除預設常式，轉而使用此類別中的自訂實作，
        # 告知 WebUI 將檔案相關操作交由此類別中的指定方法處理。
        # 或者，您可以從 inlet hook 中的請求主體直接移除檔案
        # self.file_handler = True

        # 使用特定配置初始化 'valves'。使用 'Valves' 實例有助於封裝設定，
        # 確保設定被協調管理，不會與像 'file_handler' 這樣的操作旗標混淆。
        self.valves = self.Valves()

    def inlet(self, body: dict, __user__: Optional[dict] = None) -> dict:
        """
        請求入口點 - 在聊天完成 API 處理之前修改請求主體或進行驗證。
        
        參數:
            body: 請求主體字典，包含對話訊息等資訊
            __user__: 使用者資訊字典，包含角色和設定等資訊
            
        返回:
            修改後的請求主體字典
            
        例外:
            Exception: 當對話輪數超過限制時拋出
        """
        # 輸出除錯資訊
        print(f"inlet:{__name__}")
        print(f"inlet:body:{body}")
        print(f"inlet:user:{__user__}")

        # 檢查使用者是否存在且角色為 user 或 admin
        if __user__ and __user__.get("role", "admin") in ["user", "admin"]:
            messages = body.get("messages", [])

            # 安全地取得使用者設定，避免 KeyError
            user_valves = __user__.get("valves", {})
            user_max_turns = user_valves.get("max_turns", 4)
            
            # 取得使用者設定和系統設定中的最小值作為最大對話輪數
            max_turns = min(user_max_turns, self.valves.max_turns)
            
            # 檢查是否超過最大對話輪數限制
            if len(messages) > max_turns:
                raise Exception(
                    f"對話輪數超過限制。最大輪數：{max_turns}"
                )

        return body

    def outlet(self, body: dict, __user__: Optional[dict] = None) -> dict:
        """
        回應出口點 - 在 API 處理之後修改或分析回應主體。
        
        參數:
            body: API 回應主體字典
            __user__: 使用者資訊字典
            
        返回:
            修改後的回應主體字典
        """
        # 輸出除錯資訊
        print(f"outlet:{__name__}")
        print(f"outlet:body:{body}")
        print(f"outlet:user:{__user__}")

        return body