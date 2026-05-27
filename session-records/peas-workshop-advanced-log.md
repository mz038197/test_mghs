# PEAS Workshop 進階教練紀錄

### Challenge WG-22：核心與殼分家

- **題意摘要**：在不改變終端使用體驗的前提下，把 WG-12～21 的 Agent 核心從 `main.py` 拆到 `agent_core.py`，並用 `Agent.chat()` 作為單輪對話入口。
- **實作方式**：新增 `agent_core.py`，放入 `Agent`、`Agent.from_env()`、`Agent.chat()`，並承接 ReAct、工具、JSONL、記憶整併、Skills、token 預算與 WG-21 附圖處理；改寫 `main.py` 成薄 CLI，只保留啟動、輸入迴圈、離開指令、`/image` 解析與 `agent.chat(...)` 呼叫。
- **遇到的問題**：本機專案 `.venv` 正被其他程序使用，`uv run` 嘗試更新環境時無法移除 `.venv\Scripts`；改用 `uv run --isolated` 建立臨時環境完成 import 與 CLI 無金鑰路徑驗收。
- **設計決策 / 理解**：學生確認終端體驗應維持一致；長短期記憶、Skills、裁切與核心推理都屬於 `agent_core.py`，`main.py` 不保留核心函式；`agent_core.py` 不得出現互動式 `input()`。
- **驗收結果**：
  - [x] `agent_core.py` 存在且可匯入 `Agent`，具備 `from_env` 與 `chat` — ✅ 通過。
  - [x] `main.py` 不含 `run_react_turn`、`save_session_jsonl`、`ensure_budget_before_react` 等核心函式，只呼叫 `agent.chat(...)` — ✅ 通過。
  - [x] `agent_core.py` 無實際 `input()` 呼叫 — ✅ 通過。
  - [x] 無 `OPENAI_API_KEY` 時，CLI 印出提示並結束 — ✅ 通過。
- **Agent 備註**：目前已完成 WG-22 結構拆分；若要做完整對話驗收，需要在可用金鑰與未鎖定的專案環境下跑一次多輪對話、工具呼叫與 `/image`。

### Challenge WG-22：核心與殼分家（2026-05-27 重做）

- **題意摘要**：重新把 WG-12～21 的單檔 Agent 邏輯拆成 `agent_core.py` 核心與 `main.py` CLI 殼層。
- **實作方式**：新增 `agent_core.py`，提供 `Agent.from_env()` 與 `Agent.chat(...)`，承接 ReAct、工具、JSONL、記憶整併、Skills、token 預算與 WG-21 附圖處理；`main.py` 只保留終端輸入、離開指令、`/image` 解析與 `agent.chat(...)` 呼叫。
- **遇到的問題**：本輪起點中 `main.py` 已回到 WG-21 單檔，且 `agent_core.py` 不存在；已重新建立拆檔結構。
- **設計決策 / 理解**：核心能力集中在 `agent_core.py`，CLI 只負責終端互動；第二入口可呼叫 `Agent.chat(..., on_token=...)`，不需要複製 ReAct 或 JSONL 流程。
- **驗收結果**：
  - [x] `agent_core.py` 可匯入 `Agent`，且具備 `from_env` 與 `chat` — ✅ 通過。
  - [x] `main.py` 不含 `run_react_turn`、`save_session_jsonl`、`ensure_budget_before_react` 等核心函式 — ✅ 通過。
  - [x] AST 檢查確認 `agent_core.py` 無 `input()` 呼叫，`input()` 只在 `main.py` — ✅ 通過。
  - [x] 無 `OPENAI_API_KEY` 時，`uv run --isolated main.py` 印出提示並結束 — ✅ 通過。
- **Agent 備註**：尚未使用真實金鑰跑完整多輪對話、工具呼叫與 `/image`，可在課堂驗收時補跑。
