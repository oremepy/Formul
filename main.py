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

reply_keyboard = [['Показать формулы\U0001F4DA', 'Задания\U0001F4CB'],
                  ['Помощь\U0001F4AC']]
key_for_formulas = [['Волны', 'Тепловые явления', 'Динамика'],
                    ['Электрические явления', 'Кинематика', 'Прочее'],
                    ['Назад\U0001F519']]
key_for_tasks = [['Задание 1', 'Задание 2', 'Задание 3'],
                 ['Задание 4', 'Задание 5', 'Задание 6'],
                 ['Назад\U0001F519']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
markup1 = ReplyKeyboardMarkup(key_for_formulas, one_time_keyboard=False)
markup2 = ReplyKeyboardMarkup(key_for_tasks, one_time_keyboard=False)


async def start(update, context):
    user = update.effective_user
    await update.message.reply_text(
        f"Привет {user.first_name}! Меня зовут Formul, и я помогу тебе выучить формулы.\n"
        "Если ты не понимаешь как пользоваться ботом или тебе нужна дополнительная информация о нем пиши: /help.\n",
        reply_markup=markup
    )
    return 1


async def help(update, context):
    await update.message.reply_text(
        "Сейчас ты можешь открывать любые\n"
        "формулы и учить их. Как только ты "
        "будешь готов к заданиям на "
        "закрепление этих формул, нажми "
        "на кнопку задания в первом меню. "
        "В заданиях ответ следует писать"
        " через запятую, а не через точку."
    )


async def formulas(update, context):
    await update.message.reply_text(
        "Выберете раздел в котором находится формула:",
        reply_markup=markup1
    )
    return 2


async def tasks(update, context):
    await update.message.reply_text(
        "Выберете тренировочное задание:",
        reply_markup=markup2,
    )
    return 2


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
        "Вы вернулись к первому меню",
        reply_markup=markup
    )
    return 1


async def task1(update, context):
    await update.message.reply_text(
        "Найдите плотность молока, если 206г молока занимают объем 200 см3? "
        "Ответ дайте в г/см3.\n"
        "Чтобы выйти напишите: Назад",
        reply_markup=ReplyKeyboardRemove()
    )
    return 3


async def task2(update, context):
    await update.message.reply_text(
        "Определить мощность тока в электрической лампе, если сопротивление нити акала лампы 400 Ом, а напряжение на "
        "нити 100 В. Ответ дайте в Вт.\n"
        "Чтобы выйти напишите: Назад",
        reply_markup=ReplyKeyboardRemove()
    )
    return 4


async def task3(update, context):
    await update.message.reply_text(
        "Частота колебаний крыльев вороны в полете равна в среднем 3 Гц. Сколько взмахов крыльями сделает ворона, "
        "пролетев путь 650 м со скоростью 13 м/с?\n"
        "Чтобы выйти напишите: Назад",
        reply_markup=ReplyKeyboardRemove()
    )
    return 5


async def task4(update, context):
    await update.message.reply_text(
        "В начальный момент времени тело находилось в точке с координатой 5 м, а через 2 мин от начала движения — в "
        "точке с координатой 95 м. Определите скорость тела. Ответ дайте в м/с.\n"
        "Чтобы выйти напишите: Назад",
        reply_markup=ReplyKeyboardRemove()
    )
    return 6


async def task5(update, context):
    await update.message.reply_text(
        "Груз массой 50 кг равноускоренно поднимают с помощью каната вертикально вверх в течение 2 с на высоту 10 "
        "м. Определить силу натяжения каната. Ответ дайте в Н.\n"
        "Чтобы выйти напишите: Назад",
        reply_markup=ReplyKeyboardRemove()
    )
    return 7


async def task6(update, context):
    await update.message.reply_text(
        "В железный котёл массой 5 кг налита вода массой 10 кг. Какое количество теплоты нужно передать котлу с "
        "водой для изменения их температуры от 10 до 100 °С? Ответ дайте в кДж.\n"
        "Чтобы выйти напишите: Назад",
        reply_markup=ReplyKeyboardRemove()
    )
    return 8


async def answer_correct(update, context):
    await update.message.reply_text(
        "Правильно!",
        reply_markup=markup2
    )
    return 2


async def answer_not_correct(update, context):
    await update.message.reply_text(
        "Неверный ответ, попробуйте еще раз.",
        reply_markup=ReplyKeyboardRemove()
    )


async def main_handler(update, context):
    text = update.message.text
    # chat_id = update.message.chat_id
    if text == 'Помощь\U0001F4AC':
        return await help(update, context)
    elif text == 'Старт' or text == '/start':
        return await start(update, context)
    elif text == 'Показать формулы\U0001F4DA':
        return await formulas(update, context)
    elif text == 'Задания\U0001F4CB':
        return await tasks(update, context)


async def not_main_handler(update, context):
    text = update.message.text
    # chat_id = update.message.chat_id
    if text == 'Помощь\U0001F4AC':
        return await help(update, context)
    elif text == 'Старт' or text == '/start':
        return await start(update, context)

    elif text == 'Волны':
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

    elif text == 'Задание 1':
        return await task1(update, context)
    elif text == 'Задание 2':
        return await task2(update, context)
    elif text == 'Задание 3':
        return await task3(update, context)
    elif text == 'Задание 4':
        return await task4(update, context)
    elif text == 'Задание 5':
        return await task5(update, context)
    elif text == 'Задание 6':
        return await task6(update, context)

    elif text == 'Назад\U0001F519':
        return await back(update, context)


async def check_handler1(update, context):
    text = update.message.text
    if text == '1,03':
        return await answer_correct(update, context)
    elif text == 'Назад':
        return await back(update, context)
    else:
        return await answer_not_correct(update, context)


async def check_handler2(update, context):
    text = update.message.text
    if text == '25':
        return await answer_correct(update, context)
    elif text == 'Назад':
        return await back(update, context)
    else:
        return await answer_not_correct(update, context)


async def check_handler3(update, context):
    text = update.message.text
    if text == '150':
        return await answer_correct(update, context)
    elif text == 'Назад':
        return await back(update, context)
    else:
        return await answer_not_correct(update, context)


async def check_handler4(update, context):
    text = update.message.text
    if text == '0,75':
        return await answer_correct(update, context)
    elif text == 'Назад':
        return await back(update, context)
    else:
        return await answer_not_correct(update, context)


async def check_handler5(update, context):
    text = update.message.text
    if text == '740':
        return await answer_correct(update, context)
    elif text == 'Назад':
        return await back(update, context)
    else:
        return await answer_not_correct(update, context)


async def check_handler6(update, context):
    text = update.message.text
    if text == '3987':
        return await answer_correct(update, context)
    elif text == 'Назад':
        return await back(update, context)
    else:
        return await answer_not_correct(update, context)


def main():
    conv_handler = ConversationHandler(
        # Точка входа в диалог.
        entry_points=[CommandHandler('start', start)],

        # Состояние внутри диалога.
        states={
            1: [MessageHandler(filters.TEXT & ~filters.COMMAND, main_handler)],
            2: [MessageHandler(filters.TEXT & ~filters.COMMAND, not_main_handler)],
            3: [MessageHandler(filters.TEXT & ~filters.COMMAND, check_handler1)],
            4: [MessageHandler(filters.TEXT & ~filters.COMMAND, check_handler2)],
            5: [MessageHandler(filters.TEXT & ~filters.COMMAND, check_handler3)],
            6: [MessageHandler(filters.TEXT & ~filters.COMMAND, check_handler4)],
            7: [MessageHandler(filters.TEXT & ~filters.COMMAND, check_handler5)],
            8: [MessageHandler(filters.TEXT & ~filters.COMMAND, check_handler6)],
        },

        # Точка прерывания диалога. В данном случае — команда /stop.
        fallbacks=[CommandHandler('stop', stop)]
    )
    application = Application.builder().token(BOT_TOKEN).build()
    # application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))
    # application.add_handler(CommandHandler("formulas", formulas))
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
