import base64
from credentials import config


class ChatGptService:
    def __init__(self):
        self.message_list = []


    async def send_message_list(self) -> str:
        print("Надсилаємо запит...")
        completion = await config.gpt_client.chat.completions.create(
            model="gpt-5-mini",  # gpt-4o,  gpt-4-turbo,    gpt-3.5-turbo,  GPT-4o mini
            messages=self.message_list,
            max_completion_tokens=3000,
            temperature=1
        )
        message = completion.choices[0].message
        self.message_list.append(message)
        return message.content

    def set_prompt(self, prompt_text: str) -> None:
        self.message_list.clear()
        self.message_list.append({"role": "system", "content": prompt_text})

    def add_message(self, message_text: str) -> None:
        self.message_list.append({"role": "user", "content": message_text})

    async def send_question(self, prompt_text: str, message_text: str) -> str:
        self.message_list.clear()
        self.message_list.append({"role": "system", "content": prompt_text})
        self.message_list.append({"role": "user", "content": message_text})
        return await self.send_message_list()

    async def analyze_image(self, image_data: bytearray, prompt: str = "Опиши детально, що знаходиться на цьому зображенні.", mime_type: str = "image/jpeg") -> str:
        """Аналізує зображення та повертає текстовий опис. Підтримує моделі з vision (gpt-4o, gpt-4o-mini)."""
        b64 = base64.b64encode(image_data).decode()
        messages = [
            {"role": "user", "content": [
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": {"url": f"data:{mime_type};base64,{b64}", "detail": "auto"}}
            ]}
        ]
        completion = await config.gpt_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_completion_tokens=1000,
        )
        return completion.choices[0].message.content

