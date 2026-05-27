# test-mghs

## Chainlit UI

啟動聊天介面：

```bash
uv run chainlit run chainlit_app.py -w
```

若要使用模型，請先設定 `.env` 內的 OpenAI 相關金鑰與模型名稱，並確保 `agent_core.py` 可正常建立 `Agent`。
