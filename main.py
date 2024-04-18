from config import BOT_TOKEN
import logging
from telegram.ext import Application, MessageHandler, filters, ConversationHandler
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

reply_keyboard = [['/help', '/start']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


async def start(update, contexte):
    user = update.effective_user
    await update.message.reply_text(
        f"Привет {user.first_name}! Меня зовут Formul, и я помогу тебе найти нужную формулу.\n"
        "Если ты не понимаешь как пользоваться ботом пиши: /help.\n"
        "В каком разделе находится нужная формула?",
        reply_markup=markup
    )
    return 1


async def help(update, context):
    await update.message.reply_text(
        "Боту доступны следущие команды:\n"
        "/start\n"
        "/help\n")


async def close_keyboard(update, context):
    await update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("close", close_keyboard))
    application.run_polling()


if __name__ == '__main__':
    main()
