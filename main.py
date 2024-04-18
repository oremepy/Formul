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

reply_keyboard = [['раздел1', 'раздел2'],
                  ['раздел3']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


async def start(update, contexte):
    user = update.effective_user
    await update.message.reply_text(
        rf"Привет {user.first_name}! Меня зовут Formul, и я помогу тебе найти нужную формулу. "
        "В каком разделе находится нужная формула?",
        reply_markup=markup
    )
    return 1


async def close_keyboard(update, context):
    await update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("close", close_keyboard))
    application.run_polling()
    pass


if __name__ == '__main__':
    main()
