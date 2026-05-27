import base64
import mimetypes
from pathlib import Path

import chainlit as cl
from openai import AsyncOpenAI

client = AsyncOpenAI()


def file_to_data_url(file_path: str) -> str:
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type is None:
        mime_type = "application/octet-stream"

    data = Path(file_path).read_bytes()
    encoded = base64.b64encode(data).decode("utf-8")
    return f"data:{mime_type};base64,{encoded}"


@cl.on_message
async def main(message: cl.Message):
    content = []

    if message.content:
        content.append({"type": "text", "text": message.content})

    for element in message.elements:
        mime_type = getattr(element, "mime", "") or ""
        if mime_type.startswith("image/"):
            image_url = file_to_data_url(element.path)
            content.append(
                {
                    "type": "image_url",
                    "image_url": {"url": image_url},
                }
            )

    if not content:
        await cl.Message(content="請輸入文字或上傳圖片。", author="assistant").send()
        return

    msg = cl.Message(content="")
    await msg.send()

    stream = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "你是友善的 AI 助手，請使用繁體中文回答。"},
            {"role": "user", "content": content},
        ],
        stream=True,
    )

    async for part in stream:
        token = ""
        if part.choices and part.choices[0].delta:
            token = part.choices[0].delta.content or ""
        if token:
            await msg.stream_token(token)

    await msg.update()
