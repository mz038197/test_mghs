import os
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()


def main():
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("OPENAI_API_KEY is not set")
        return

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        api_key=api_key,
    )

    response = llm.invoke("你好,你好嗎?")
    print(response.content)


if __name__ == "__main__":
    main()
