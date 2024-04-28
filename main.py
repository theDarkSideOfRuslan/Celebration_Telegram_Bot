import logging
from telegram.ext import Application, MessageHandler, filters
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)
logger = logging.getLogger(__name__)
day_select_keyboard = [['День\nРождения', 'Новый\nГод'], ['23 Февраля', '8 марта'], ['1 Мая', 'День\nПобеды']]
all_days = [j for i in day_select_keyboard for j in i]
print(all_days)
day_select_markup = ReplyKeyboardMarkup(day_select_keyboard, one_time_keyboard=True)


async def start(update, context):
    await update.message.reply_text(
        "Доброго времени суток! \n\nЯ создам открытку: выберите праздник",
        reply_markup=day_select_markup
    )


async def help(update, context):
    await update.message.reply_text(
        "Введите /start, чтобы начать создавать открытку")


async def answer(update, context):
    # update.message.text
    await update.message.reply_text(
        "Я бот справочник."
    )


async def close_keyboard(update, context):
    await update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )


def main():
    application = Application.builder().token('7022244531:AAFrriCDnwrrQFPNsmzhEPYbKWP0gIqebgc').build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("close", close_keyboard))
    text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, answer)
    application.add_handler(text_handler)
    application.run_polling()


if __name__ == '__main__':
    main()
