from config import BOT_TOKEN, URL_DYNAMIC, URL_WAVES, URL_THERMAL, URL_KINEMATIC, URL_OTHER, URL_ELECTRIC
import logging
from telegram.ext import Application, MessageHandler, filters, ConversationHandler
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

reply_keyboard = [['Помощь', 'Старт'],
                  ['Показать формулы', 'Задания']]
reply_key2 = [['Волны', 'Тепловые явления', 'Динамика'],
              ['Электрические явления', 'Кинематика', 'Прочее'],
              ['Назад']]
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
    return 1


async def help(update, context):
    await update.message.reply_text(
        "Боту доступны следущие команды:\n"
        "/start\n"
        "/help\n"
        "/close\n"
        "/tasks\n"
        "/show_formulas\n"
        "/back\n")
    return 1


async def show_formulas(update, context):
    await update.message.reply_text(
        "Выберете раздел в котором находится формула:",
        reply_markup=markup1
    )
    return 2


async def tasks(update, context):
    await update.message.reply_text(
        "Выберете тренировочное задание:")
    return 1


async def waves(update, context):
    await update.message.reply_text(
        "Колебания и волны:")
    await update.message.reply_photo(
        photo=URL_WAVES
    )
    return 2


async def thermal(update, context):
    await update.message.reply_text(
        "Тепловые явления:")
    await update.message.reply_photo(
        photo=URL_THERMAL
    )
    return 2


async def dynamic(update, context):
    await update.message.reply_text(
        "Динамика, законы сохранения:")
    await update.message.reply_photo(
        photo=URL_DYNAMIC
    )
    return 2


async def electric(update, context):
    await update.message.reply_text(
        "Электрические явления:")
    await update.message.reply_photo(
        photo=URL_ELECTRIC
    )
    return 2


async def kinematic(update, context):
    await update.message.reply_text(
        "Кинематика:")
    await update.message.reply_photo(
        photo=URL_KINEMATIC
    )
    return 2


async def other(update, context):
    await update.message.reply_text(
        "Прочие формулы за 7 класс:")
    await update.message.reply_photo(
        photo=URL_OTHER
    )
    return 2


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
    return 1


async def main_handler(update, context):
    text = update.message.text
    # chat_id = update.message.chat_id
    if text == 'Помощь':
        return await help(update, context)
    elif text == 'Старт':
        return await start(update, context)
    elif text == 'Показать формулы':
        return await show_formulas(update, context)
    elif text == 'Задания':
        return await tasks(update, context)


async def not_main_handler(update, context):
    text = update.message.text
    # chat_id = update.message.chat_id
    if text == 'Волны':
        return await waves(update, context)
    elif text == 'Тепловые явления':
        return await thermal(update, context)
    elif text == 'Динамика':
        return await dynamic(update, context)
    elif text == 'Электрические явления':
        return await electric(update, context)
    elif text == 'Кинематика':
        return await kinematic(update, context)
    elif text == 'Прочее':
        return await other(update, context)
    elif text == 'Назад':
        return await back(update, context)


def main():
    conv_handler = ConversationHandler(
        # Точка входа в диалог.
        entry_points=[CommandHandler('start', start)],

        # Состояние внутри диалога.
        states={
            1: [MessageHandler(filters.TEXT & ~filters.COMMAND, main_handler)],
            2: [MessageHandler(filters.TEXT & ~filters.COMMAND, not_main_handler)],
        },

        # Точка прерывания диалога. В данном случае — команда /stop.
        fallbacks=[CommandHandler('stop', stop)]
    )
    application = Application.builder().token(BOT_TOKEN).build()
    # application.add_handler(CommandHandler("start", start))
    # application.add_handler(CommandHandler("help", help))
    # application.add_handler(CommandHandler("show_formulas", show_formulas))
    # application.add_handler(CommandHandler("tasks", tasks))
    # application.add_handler(CommandHandler("waves", waves))
    # application.add_handler(CommandHandler("thermal", thermal))
    # application.add_handler(CommandHandler("dynamic", dynamic))
    # application.add_handler(CommandHandler("kinematic", kinematic))
    # application.add_handler(CommandHandler("electric", electric))
    # application.add_handler(CommandHandler("other", other))
    application.add_handler(CommandHandler("back", back))
    application.add_handler(CommandHandler("close", close_keyboard))
    application.add_handler(conv_handler)
    application.run_polling()


if __name__ == '__main__':
    main()
