import logging
from telegram.ext import Application, MessageHandler, filters
from telegram.ext import CommandHandler, ConversationHandler
from telegram import ReplyKeyboardMarkup
import photo_generator


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

day_select_keyboard = [['День\nРождения', 'Новый\nГод'], ['23 Февраля', '8 марта'], ['1 Мая', 'День\nПобеды']]
all_days = [j for i in day_select_keyboard for j in i]
print(all_days)
day_select_markup = ReplyKeyboardMarkup(day_select_keyboard, one_time_keyboard=True)
continue_keyboard = [['Продолжить']]
continue_markup = ReplyKeyboardMarkup(continue_keyboard, one_time_keyboard=True)


async def start(update, context):
    await update.message.reply_text(
        "Доброго времени суток, я создам открытку!\nНажмите продолжить",
        reply_markup=continue_markup
    )
    return 1


async def day_select(update, context):
    await update.message.reply_text(
        'Выберите праздник:',
        reply_markup=day_select_markup
    )
    return 2


async def by_select(update, context):
    context.user_data['day'] = update.message.text.replace('\n', ' ')
    await update.message.reply_text(
        f"открытка от:"
    )
    return 3


async def to_select(update, context):
    context.user_data['by'] = update.message.text
    await update.message.reply_text(
        f"открытка кому:"
    )
    return 4


async def photo_generate(update, context):
    context.user_data['to'] = update.message.text
    #Тут все картинки как python объекты, в 'data/NewYear' сохраняются открытки
    photos = photo_generator.new_year(context.user_data['by'], context.user_data['to'])
    await update.message.reply_text(
        open('data/NewYear/NewYear33.jpg'),
        f"Делаем открытку на праздник {context.user_data['day']} от: {context.user_data['by']} кому: {context.user_data['to']}"
    )
    context.user_data.clear()
    return ConversationHandler.END


async def stop(update, context):
    await update.message.reply_text("Всего доброго!")
    return ConversationHandler.END


async def help(update, context):
    await update.message.reply_text(
        "Введите /start, чтобы начать создавать открытку")


def main():
    application = Application.builder().token('7022244531:AAFrriCDnwrrQFPNsmzhEPYbKWP0gIqebgc').build()
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            1: [MessageHandler(filters.TEXT & ~filters.COMMAND, day_select)],
            2: [MessageHandler(filters.TEXT & ~filters.COMMAND, by_select)],
            3: [MessageHandler(filters.TEXT & ~filters.COMMAND, to_select)],
            4: [MessageHandler(filters.TEXT & ~filters.COMMAND, photo_generate)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )
    application = Application.builder().token('7022244531:AAFrriCDnwrrQFPNsmzhEPYbKWP0gIqebgc').build()
    application.add_handler(conv_handler)
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))
    application.run_polling()

if __name__ == '__main__':
    main()
