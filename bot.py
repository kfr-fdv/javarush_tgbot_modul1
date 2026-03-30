from telegram import Update, BotCommand, BotCommandScopeChat, ReplyKeyboardRemove
from telegram.ext import filters, ApplicationBuilder, CallbackQueryHandler, ContextTypes, CommandHandler, \
    ConversationHandler, MessageHandler, PicklePersistence

from conversations.gpt_dialog import get_gpt_dialog_conversation_handler
from conversations.talk_dialog import get_talk_dialog_conversation_handler
from conversations.image_to_text import get_image_to_text_handler
from conversations.quiz import get_quiz_conversation_handler
from conversations.translate import get_translate_conversation_handler
from gpt import ChatGptService
from states_test import get_profile_conversation_handler
from util import (load_message, send_text, send_image, show_main_menu,
                  default_callback_handler, load_prompt, get_ai_service)
from credentials import config
from keyboards.talk_with_famous_people import inline_actors, ACTORS
from keyboards.gpt_dialog import get_finish_keyboard

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = load_message('main')
    await send_image(update, context, 'main')
    await send_text(update, context, text)
    await show_main_menu(update, context, {
        'start': 'Головне меню',
        'random': 'Дізнатися випадковий цікавий факт 🧠',
        'gpt': 'Задати питання чату GPT 🤖',
        'image_to_text': 'Опис зображення 📷',
        'talk': 'Поговорити з відомою особистістю 👤',
        'quiz': 'Взяти участь у квізі ❓',
        'translate': 'Перекладіть своє повідомлення на обрану мову',
        'movie': 'Допомога з вибором фільму'
        # Додати команду в меню можна так:
        # 'command': 'button text'

    })

    context.user_data["ai_service"] = ChatGptService()

async def random(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = load_prompt("random")
    message = await update.message.reply_text("Зачекайте декілька секунд...")

    chat_gpt = ChatGptService()

    chat_gpt.set_prompt(prompt)
    response_text = await chat_gpt.send_message_list()
    await message.edit_text(response_text)

async def gpt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = load_message('gpt')
    await send_image(update, context, 'gpt')

    await update.message.reply_text(
        text,
        reply_markup=get_finish_keyboard()
    )
    # request = update.message.text.strip()



async def talk(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Оберіть відому особистість, з якою хочете поговорити:", reply_markup=inline_actors)


app = (
    ApplicationBuilder()
    .token(config.token)
    .concurrent_updates(True)
    .persistence(PicklePersistence(filepath="user_data.pickle"))
    .build()
)

app.add_handler(CommandHandler('start', start))
app.add_handler(CommandHandler('random', random))
app.add_handler(CommandHandler('gpt', gpt))
app.add_handler(CommandHandler('talk', talk))

app.add_handler(get_profile_conversation_handler())
app.add_handler(get_gpt_dialog_conversation_handler())
app.add_handler(get_image_to_text_handler())

app.add_handler(get_quiz_conversation_handler())
app.add_handler(get_translate_conversation_handler())

app.add_handler(get_talk_dialog_conversation_handler())


print("Bot started...")
app.run_polling()