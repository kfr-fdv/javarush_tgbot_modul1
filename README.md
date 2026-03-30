# 🤖 javarush_tgbot_modul1

Навчальний Telegram-бот, який інтегрує ChatGPT для різних сценаріїв: від квізів і перекладу текстів до спілкування з відомими особистостями, рекомендацій та розпізнавання зображень.

---

## 📂 Структура проєкту
resources/

├── images/      # Зображення для повідомлень
├── messages/    # Текстові повідомлення для клієнта
└── prompts/     # Системні промти для GPT


conversations/   # Сценарії діалогів (quiz, talk, translate, gpt, image_to_text, movie))

keyboards/       # Клавіатури для різних сценаріїв

credentials/     # Конфігурація токенів (.env)

bot.py           # Головний файл запуску

config.py        # Конфігурація

gpt.py           # Логіка роботи з ChatGPT

util.py          # Утилітарні функції

requirements.txt # Залежності

README.md        # Документація

---

## ⚙️ Налаштування

1. Створи файл `.env` у корені проєкту та додай туди свої ключі:

BOTTOKEN=your_telegram_bot_tokenn
ChatGPT_TOKEN=your_openai_api_key

2. У файлі `credentials/config.py` використовується `dotenv` для завантаження цих змінних:

```python
from dotenv import load_dotenv
import os
from openai import AsyncOpenAI

load_dotenv()

class Config:
    token = os.getenv("BOT_TOKEN")
    gpt_token = os.getenv("ChatGPT_TOKEN")
    gpt_client = AsyncOpenAI(api_key=gpt_token)

config = Config()
```
2. У файлі `credentials/config.py` використовується `dotenv` для завантаження цих змінних:

```python
from dotenv import load_dotenv
import os
from openai import AsyncOpenAI

load_dotenv()

class Config:
    token = os.getenv("BOT_TOKEN")
    gpt_token = os.getenv("ChatGPT_TOKEN")
    gpt_client = AsyncOpenAI(api_key=gpt_token)

config = Config()
```

2. У файлі `credentials/config.py` використовується `dotenv` для завантаження цих змінних:

```python
from dotenv import load_dotenv
import os
from openai import AsyncOpenAI

load_dotenv()

class Config:
    token = os.getenv("BOT_TOKEN")
    gpt_token = os.getenv("ChatGPT_TOKEN")
    gpt_client = AsyncOpenAI(api_key=gpt_token)

config = Config()
```
3. Додай `.nv у `.gitignore щоб він не потрапив у репозиторій.

🚀 Встановлення та запуск
```bash
git clone https://github.com/username/javarush_tgbot_modul1.git
cd javarush_tgbot_modul1
pip install -r requirements.txt
python main.py
```

✨ Функціонал
1. Випадковий факт (`/random`)

- Надсилає заздалегідь підготовлене зображення.
- Робить запит до ChatGPT із промтом.
- Відповідь надсилається користувачеві.
- Кнопки:
	- Закінчити → працює як `/start
	- Хочу ще факт → працює як /random.


---
2. ChatGPT інтерфейс (`/gpt`)

- Надсилає зображення.
- Передає текст повідомлення користувача до ChatGPT.
- Відповідь повертається текстом.

---
3. Діалог з відомою особистістю (`/talk`)

- Надсилає зображення та пропонує вибір особистості через кнопки.
- Встановлює промт для GPT відповідно до вибраної особистості.
- Подальші повідомлення користувача передаються GPT.
- Кнопка Закінчити → працює як /start.


---
4.  Взяти участь у квізі (`/quiz`)
- Необхідно вибір тему.
- Для вибору теми користувач повинен написати в чаті ключове слово:
  - `quiz_prog` → питання з Python
  - `quiz_math` → питання з математики
  - `quiz_biology` → питання з біології
  - `quiz_more` → наступне питання на ту ж тему
- GPT генерує питання, користувач відповідає, бот перевіряє відповідь.
- Якщо відповідь правильна → «Правильно!»
- Якщо неправильна → «Неправильно! Правильна відповідь – {answer}».
- Бот веде рахунок правильних відповідей.
- Кнопки:
  - **Ще питання** → продовжує квіз.
  - **Змінити тему** → повертає до вибору теми.
  - **Закінчити** → завершує квіз.


---
5. Перекладач (`/translate`)

- Пропонує вибір мови через кнопки.
- Користувач надсилає текст.
- GPT перекладає текст у вибрану мову.

- Кнопки:
	- Змінити мову → повертає до вибору мови.
	- Закінчити → працює як `/start

---
6.  Опис зображення (`/image_to_text`)

- Користувач надсилає фото.
- GPT аналізує зображення та описує його текстом.
- Відповідь надсилається користувачеві.

---
7.  Допомога з вибором фільму (`/movie`)
- Бот запитує жанр і додаткові побажання.
- GPT формує рекомендації та надсилає їх користувачеві.
---
🛠️ Технології

- Python 3.10+
- python-telegram-bot
- OpenAI API
- dotenv для керування токенами

---
