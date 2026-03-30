from dotenv import load_dotenv
import os
from openai import AsyncOpenAI

load_dotenv()


class Config:
    token = os.getenv("BOT_TOKEN")
    gpt_token = os.getenv("ChatGPT_TOKEN")
    gpt_client = AsyncOpenAI(api_key=gpt_token)

config = Config()