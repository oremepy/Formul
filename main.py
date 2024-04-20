from config import BOT_TOKEN, URL_DYNAMIC, URL_WAVES, URL_THERMAL
import logging
import requests
from telegram.ext import Application, MessageHandler, filters, ConversationHandler
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

reply_keyboard = [['/help', '/start'],
                  ['/show_formulas', '/tasks']]
reply_key2 = [['/waves', '/thermal', '/chapter3'],
              ['/back']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
markup1 = ReplyKeyboardMarkup(reply_key2, one_time_keyboard=False)


async def start(update, context):
    user = update.effective_user
    await update.message.reply_text(
        f"Привет {user.first_name}! Меня зовут Formul, и я помогу тебе найти нужную формулу.\n"
        "Если ты не понимаешь как пользоваться ботом пиши: /help.\n"
        "В каком разделе находится нужная формула?",
        reply_markup=markup
    )


async def help(update, context):
    await update.message.reply_text(
        "Боту доступны следущие команды:\n"
        "/start\n"
        "/help\n"
        "/close\n"
        "/tasks\n"
        "/show_formulas\n"
        "/back\n")


async def show_formulas(update, context):
    await update.message.reply_text(
        "Выберете раздел в котором находится формула:",
        reply_markup=markup1
    )
    return 1


async def tasks(update, context):
    await update.message.reply_text(
        "Выберете тренировочное задание:")


async def waves(update, context):
    await update.message.reply_text(
        "Колебания и волны:")
    await update.message.reply_photo(
        photo=URL_WAVES
    )
    return ConversationHandler.END


async def thermal(update, context):
    await update.message.reply_text(
        "Тепловые явления:")
    await update.message.reply_photo(
        photo=URL_THERMAL
    )
    return ConversationHandler.END


async def dynamic(update, context):
    await update.message.reply_text(
        "Динамика, законы сохранения:")
    await update.message.reply_photo(
        photo=URL_DYNAMIC
    )
    return ConversationHandler.END


async def close_keyboard(update, context):
    await update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )


async def stop(update, context):
    await update.message.reply_text("Всего доброго!")
    return ConversationHandler.END


async def back(update, context):
    await update.message.reply_text(
        "Ok",
        reply_markup=markup
    )
    return ConversationHandler.END


conv_handler = ConversationHandler(
    # Точка входа в диалог.
    # В данном случае — команда /start. Она задаёт первый вопрос.
    entry_points=[CommandHandler('show_formulas', show_formulas)],

    # Состояние внутри диалога.
    # Вариант с двумя обработчиками, фильтрующими текстовые сообщения.
    states={
        # Функция читает ответ на первый вопрос и задаёт второй.
        1: [MessageHandler(filters.TEXT & ~filters.COMMAND, waves)],
        # Функция читает ответ на второй вопрос и завершает диалог.
        2: [MessageHandler(filters.TEXT & ~filters.COMMAND, thermal)],
        3: [MessageHandler(filters.TEXT & ~filters.COMMAND, dynamic)]
    },

    # Точка прерывания диалога. В данном случае — команда /stop.
    fallbacks=[CommandHandler('stop', stop)]
)


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("show_formulas", show_formulas))
    application.add_handler(CommandHandler("tasks", tasks))
    application.add_handler(CommandHandler("waves", waves))
    application.add_handler(CommandHandler("thermal", thermal))
    application.add_handler(CommandHandler("chapter3", dynamic))
    application.add_handler(CommandHandler("back", back))
    application.add_handler(CommandHandler("close", close_keyboard))
    application.add_handler(conv_handler)
    application.run_polling()


if __name__ == '__main__':
    main()
