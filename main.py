import logging
from telegram.ext import Application, MessageHandler, filters
from telegram.ext import CommandHandler, ConversationHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)
logger = logging.getLogger(__name__)

day_select_keyboard = [['День\nРождения', 'Новый\nГод'], ['23 Февраля', '8 марта'], ['1 Мая', 'День\nПобеды']]
day_select_markup = ReplyKeyboardMarkup(day_select_keyboard, one_time_keyboard=True)
all_days = [j for i in day_select_keyboard for j in i]
print(all_days)


continue_keyboard = [['Продолжить']]
continue_markup = ReplyKeyboardMarkup(continue_keyboard, one_time_keyboard=True)


async def start(update, context):
    await update.message.reply_text(
        "Доброго времени суток! \n\nЯ создам открытку!",
        reply_markup = continue_markup
    )
    return 1


async def day_selector(update, context):
    await update.message.reply_text(
        "Выберите праздник:",
        reply_markup = day_select_markup
    )
    return 2


async def by_selector(update, context):
    context.user_data['day'] = update.message.text.replace('\n', ' ')
    await update.message.reply_text(
        'Введите ваше имя:')
    return 3


async def to_selector(update, context):
    context.user_data['by'] = update.message.text
    await update.message.reply_text(
        'Введите имя получателя:')
    return 4


async def image_generator(update, context):
    context.user_data['to'] = update.message.text
    await update.message.reply_text(
        f'создаю открытку на праздник {context.user_data['day']} от {context.user_data['by']} для {context.user_data['to']}')
    return ConversationHandler.END


async def help(update, context):
    await update.message.reply_text(
        "Введите /start, чтобы начать создавать открытку")


async def close_keyboard(update, context):
    await update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )


async def stop(update, context):
    await update.message.reply_text("Всего доброго!")
    return ConversationHandler.END



def main():
    application = Application.builder().token('7022244531:AAFrriCDnwrrQFPNsmzhEPYbKWP0gIqebgc').build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            1: [MessageHandler(filters.TEXT & ~filters.COMMAND, day_selector)],
            2: [MessageHandler(filters.TEXT & ~filters.COMMAND, by_selector)],
            3: [MessageHandler(filters.TEXT & ~filters.COMMAND, to_selector)],
            4: [MessageHandler(filters.TEXT & ~filters.COMMAND, image_generator)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )
    application.add_handler(conv_handler)

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))
    application.run_polling()


if __name__ == '__main__':
    main()
