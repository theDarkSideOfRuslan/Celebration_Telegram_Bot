import logging
import os
from telegram.ext import Application, MessageHandler, filters, \
    CommandHandler, ConversationHandler
from telegram import ReplyKeyboardMarkup, Update, InputMediaPhoto
import photo_generator


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

day_select_keyboard = [['День\nРождения', 'Новый\nГод'], ['23 Февраля', '8 марта'], ['1 Мая', 'День\nПобеды']]
all_days = list(map(lambda x: x.replace('\n', ' '), [j for i in day_select_keyboard for j in i]))
print(all_days)
day_select_markup = ReplyKeyboardMarkup(day_select_keyboard, one_time_keyboard=True)
continue_keyboard = [['Продолжить']]
continue_markup = ReplyKeyboardMarkup(continue_keyboard, one_time_keyboard=True)


async def start(update: Update, context):
    context.user_data.clear()
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
    if context.user_data['day'] not in all_days:
        await update.message.reply_text(
            f"Такого праздника нет, давай заново :) /start"
        )
        return ConversationHandler.END
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
    id = update.message.chat_id
    day, by, to = context.user_data['day'], context.user_data['by'], context.user_data['to']
    context.user_data.clear()
    if day not in all_days:
        await update.message.reply_text(
            f"Такого праздника нет, давай заново :) /start"
        )
        context.user_data.clear()
        return ConversationHandler.END

    await update.message.reply_text(
        f'Делаем открытку для праздника "{day}" от: "{by}" кому: "{to}"'
    )
    if day == 'Новый Год':
        photo_generator.new_year(by, to, id)
        photos = [InputMediaPhoto(open(f'data/NewYear/NewYear1_{id}.jpg', 'rb')),
                 InputMediaPhoto(open(f'data/NewYear/NewYear2_{id}.jpg', 'rb')),
                 InputMediaPhoto(open(f'data/NewYear/NewYear3_{id}.jpg', 'rb')),
                 InputMediaPhoto(open(f'data/NewYear/NewYear4_{id}.jpg', 'rb'))
                 ]
        await update.message.reply_media_group(
            photos
        )
        for i in range(len(photos)):
            os.remove(f'data/NewYear/NewYear{i + 1}_{id}.jpg')
    elif day == 'День Рождения':
        photo_generator.birthday(by, to, id)
        photos = [InputMediaPhoto(open(f'data/Birthday/Birthday1_{id}.jpg', 'rb')),
                  InputMediaPhoto(open(f'data/Birthday/Birthday2_{id}.jpg', 'rb'))
                  ]
        await update.message.reply_media_group(
            photos
        )
        for i in range(len(photos)):
            os.remove(f'data/Birthday/Birthday{i + 1}_{id}.jpg')
    elif day == '8 марта':
        photo_generator.march8th(by, to, id)
        photos = [InputMediaPhoto(open(f'data/March8th/March8th1_{id}.jpg', 'rb')),
                  InputMediaPhoto(open(f'data/March8th/March8th2_{id}.jpg', 'rb'))
                  ]
        await update.message.reply_media_group(
            photos
        )
        for i in range(len(photos)):
            os.remove(f'data/March8th/March8th{i + 1}_{id}.jpg')
    elif day == '23 Февраля':
        photo_generator.February23rd(by, to, id)
        photos = [InputMediaPhoto(open(f'data/February23rd/February23rd1_{id}.jpg', 'rb')),
                  InputMediaPhoto(open(f'data/February23rd/February23rd2_{id}.jpg', 'rb'))
                  ]
        await update.message.reply_media_group(
            photos
        )
        for i in range(len(photos)):
            os.remove(f'data/February23rd/February23rd{i + 1}_{id}.jpg')
    elif day == '1 Мая':
        photo_generator.May1st(by, to, id)
        photos = [InputMediaPhoto(open(f'data/May1st/May1st1_{id}.jpg', 'rb')),
                  InputMediaPhoto(open(f'data/May1st/May1st2_{id}.jpg', 'rb'))
                  ]
        await update.message.reply_media_group(
            photos
        )
        for i in range(len(photos)):
            os.remove(f'data/May1st/May1st{i + 1}_{id}.jpg')
    elif day == 'День Победы':
        photo_generator.May9th(by, to, id)
        photos = [InputMediaPhoto(open(f'data/May9th/May9th1_{id}.jpg', 'rb')),
                  InputMediaPhoto(open(f'data/May9th/May9th2_{id}.jpg', 'rb')),
                  InputMediaPhoto(open(f'data/May9th/May9th3_{id}.jpg', 'rb'))
                  ]
        await update.message.reply_media_group(
            photos
        )
        for i in range(len(photos)):
            os.remove(f'data/May9th/May9th{i + 1}_{id}.jpg')
    context.user_data.clear()
    return ConversationHandler.END


async def stop(update, context):
    await update.message.reply_text("Всего доброго!")
    context.user_data.clear()
    return ConversationHandler.END


async def help(update, context):
    await update.message.reply_text(
        "Введите /start, чтобы начать создавать открытку")


def main():
    application = Application.builder().token('7048582906:AAHuQrWm6pAFbOYoxa2zfwSc2XgYO1NTM7w').build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            1: [MessageHandler(filters.TEXT & ~filters.COMMAND, day_select)],
            2: [MessageHandler(filters.TEXT & ~filters.COMMAND, by_select)],
            3: [MessageHandler(filters.TEXT & ~filters.COMMAND, to_select)],
            4: [MessageHandler(filters.TEXT & ~filters.COMMAND, photo_generate)]
        },
        fallbacks=[CommandHandler('stop', stop), CommandHandler("start", start)]
    )
    application.add_handler(conv_handler)
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))
    application.run_polling()

if __name__ == '__main__':
    main()