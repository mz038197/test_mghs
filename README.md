# test-mghs

## Chainlit UI

啟動聊天介面：

```bash
uv run python scripts/run_chainlit.py
```

或手動指定其他連接埠：

```bash
uv run chainlit run chainlit_app.py --port 8001
```

功能：
- 文字聊天
- 直接上傳圖片並一起送給模型
- 使用 Chainlit 內建聊天介面

如果 `.env` 尚未設定 OpenAI API key，請先補上後再啟動。

## Gradio UI

啟動 Gradio 版本：

```bash
uv run python gradio_app.py
```

特色：
- 左側選單區
- 中間聊天區
- 圖片上傳
- 串流輸出

## 舊版 Streamlit

如果仍要使用舊版 Streamlit：

```bash
uv run streamlit run streamlit_app.py
```
