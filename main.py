import os
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()


def main():
    agent_name = "法鬥超人"
    welcome_message = f"歡迎!我是{agent_name},請問有什麼可以幫你的嗎?"
    print(welcome_message)


if __name__ == "__main__":
    main()



