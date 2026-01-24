"""
title: 對話輪次限制過濾器
author: open-webui
author_url: https://github.com/open-webui
funding_url: https://github.com/open-webui
version: 0.1
description: 限制使用者對話輪次的過濾器，防止過度使用
"""

from typing import Optional, Dict, Any

# 簡化的 BaseModel 和 Field 實現，避免 pydantic 依賴
class SimpleBaseModel:
    """簡單的 BaseModel 實現"""
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

def Field(default=None, description=None):
    """簡單的 Field 實現"""
    return default

# 使用簡化實現替代 pydantic
BaseModel = SimpleBaseModel


class Filter:
    """
    對話輪次限制過濾器
    
    此過濾器用於控制使用者的對話輪次，防止系統被過度使用。
    支援全域設定和使用者個人化設定。
    """

    class Valves(BaseModel):
        """全域閥值設定"""
        def __init__(self):
            self.priority = 0  # 過濾器優先級等級
            self.max_turns = 8  # 全域最大允許對話輪次數量

    class UserValves(BaseModel):
        """使用者個人化閥值設定"""
        def __init__(self):
            self.max_turns = 4  # 使用者個人最大允許對話輪次數量

    def __init__(self):
        """
        初始化過濾器
        
        設定閥值和配置參數。如需自訂檔案處理邏輯，
        可取消註解 self.file_handler = True
        """
        # 自訂檔案處理邏輯標誌。此標誌有助於繞過預設常式，
        # 改用此類別中的指定方法，告知 WebUI 將檔案相關操作
        # 委派給此類別內的指定方法。或者，您可以從 inlet
        # hook 中直接從請求主體移除檔案
        # self.file_handler = True

        # 使用特定配置初始化 'valves'。使用 'Valves' 實例
        # 有助於封裝設定，確保設定被協調管理，
        # 不會與 'file_handler' 等操作標誌混淆
        self.valves = self.Valves()

    def inlet(self, body: Dict[str, Any], __user__: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        請求入口處理器
        
        在聊天完成 API 處理前修改請求主體或進行驗證。
        此函數是 API 的前處理器，可對輸入執行各種檢查，
        也可在發送至 API 前修改請求。
        
        Args:
            body: API 請求主體
            __user__: 使用者資訊字典
            
        Returns:
            dict: 處理後的請求主體
            
        Raises:
            Exception: 當對話輪次超過限制時拋出異常
        """
        print(f"入口處理:{__name__}")
        print(f"入口處理:請求主體:{body}")
        print(f"入口處理:使用者:{__user__}")

        # 檢查使用者角色權限
        if __user__ and __user__.get("role", "admin") in ["user", "admin"]:
            messages = body.get("messages", [])

            # 取得全域和使用者設定的最小值作為限制
            max_turns = min(__user__["valves"].max_turns, self.valves.max_turns)
            
            # 檢查對話輪次是否超過限制
            if len(messages) > max_turns:
                raise Exception(f"對話輪次超過限制。最大輪次數: {max_turns}")

        return body

    def outlet(self, body: Dict[str, Any], __user__: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        響應出口處理器
        
        在 API 處理後修改或分析響應主體。
        此函數是 API 的後處理器，可用於修改響應
        或執行額外的檢查和分析。
        
        Args:
            body: API 響應主體
            __user__: 使用者資訊字典
            
        Returns:
            dict: 處理後的響應主體
        """
        print(f"出口處理:{__name__}")
        print(f"出口處理:響應主體:{body}")
        print(f"出口處理:使用者:{__user__}")

        return body