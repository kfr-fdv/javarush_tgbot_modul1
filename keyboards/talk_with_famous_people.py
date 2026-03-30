from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


ACTORS = {
    "talk_cobain": "Курт Кобейн - Соліст гурту Nirvana 🎸",
    "talk_queen": "Єлизавета II - Королева Об'єднаного Королівства 👑",
    "talk_tolkien": "Джон Толкін - Автор книги 'Володар Перснів' 📖",
    "talk_nietzsche": "Фрідріх Ніцше - Філософ 🧠",
    "talk_hawking": "Стівен Гокінг - Фізик 🔬"
}

inline_actors = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text=label, callback_data=f"actor_{key}")]
     for key, label in ACTORS.items()]
)

