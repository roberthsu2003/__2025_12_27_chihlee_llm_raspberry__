## RAG 系統測試問題集

### 1. 精準數據提取測試
**目標：** 驗證系統從文檔中準確提取特定技術規格的能力

**英文問題：**
"How long does the battery of SonicCloud 9 last with ANC turned on?"

**中文問題：**
"開啟主動降噪功能後，SonicCloud 9 的電池續航時間為何？"

**預期答案：** 30 小時

---

### 2. 跨文檔資訊區分測試
**目標：** 測試系統區分不同產品文檔中相似概念的能力

**英文問題：**
"What does a flashing red light mean on the SonicCloud 9 versus the FloraGard Pro?"

**中文問題：**
"SonicCloud 9 耳機與 FloraGard Pro 植物監測器的閃爍紅燈指示分別代表什麼？"

**預期答案：** 
- SonicCloud 9：電量不足
- FloraGard Pro：土壤水分嚴重不足

---

### 3. 故障排除流程測試
**目標：** 驗證系統提供完整解決方案的能力

**英文問題：**
"My BrewBot X1 is showing error code E02. What should I do?"

**中文問題：**
"我的 BrewBot X1 咖啡機顯示錯誤代碼 E02，應如何處理？"

**預期答案：** 研磨機卡住，請清理咖啡豆漏斗

---

### 4. 資訊完整性驗證測試
**目標：** 測試系統正確識別不存在資訊的能力（避免幻覺）

**英文問題：**
"Does the BrewBot X1 support 5GHz WiFi?"

**中文問題：**
"BrewBot X1 咖啡機是否支援 5GHz WiFi 網路？"

**預期答案：** 否，僅支援 2.4GHz WiFi

