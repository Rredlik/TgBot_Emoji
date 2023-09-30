import asyncio

from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message

from telegram_bot.database.methods.create import new_message
from telegram_bot.database.methods.update import update_message
from user_bot.filters import get_vip_filters
from user_bot.handlers.my.main import checkMessageType
from user_bot.utils import cmd


@cmd()
async def __userName(app: Client, msg: Message):
    userData = await app.get_me()
    print(userData.first_name if not None else userData.username)

    # asyncio.run(await userName(app, msg))


async def userName(app: Client, msg: Message):
    strokes = (
        "S",
        "Sk",
        "Ski",
        "Skid",
        "Skidi",
        "Skidik",
        "Skidiki",
        "Skidikis",
        "👾Skidikis",
        "S👾kidikis",
        "Sk👾idikis",
        "Ski👾dikis",
        "Skid👾ikis",
        "Skidi👾kis",
        "Skidik👾is",
        "Skidiki👾s",
        "Skidikis👾",
        "🦄Skidikis👾",
    )
    await msg.delete()

    for stroke in strokes:
        await asyncio.sleep(0.5)
        await app.update_profile(first_name=stroke)


async def __importChat(app: Client, msg: Message):
    count = 0
    user = await app.get_me()  # 35....
    chat_id = 1241977405  # 5531606682

    async for message in app.get_chat_history(chat_id):
        date = message.date

        fromUser_id = message.from_user.id
        if fromUser_id == chat_id:
            to_user_id = user.id
        else:
            to_user_id = chat_id

        text, msg_id = await checkMessageType(app, message)
        # print(f'chat_owner_id={user.id}, date={date}, from_user_id={fromUser_id}, to_user_id={to_user_id},'
        #       f'message_text= {text}, message_id= {msg_id}')

        # Для обновления id файлов
        # # if text is None:
        # #     continue
        # # msg_type = text.split('|')[0]
        # # if msg_type == 'photo' or msg_type == 'video' or msg_type == 'voice' \
        # #         or msg_type == 'video_note' or msg_type == 'sticker':
        # #     if update_message(chat_owner_id=user.id, message_text=text, message_id=msg_id):

        if new_message(chat_owner_id=user.id, date=date, from_user_id=fromUser_id, to_user_id=to_user_id,
                       message_text=text, message_id=msg_id):
            count += 1

    await app.send_message(user.id, text=f'✅ Сохранено {count} сообщений\n'
                                         f'Дата: {str(date)}\n'
                                         f'Текст: {text}')


# async def __sendMsgById(app: Client, msg: Message):
#     await app.send_photo(5531606682, photo=f'AgACAgIAAxkBAAEC3bxlFVmHU9mGFF0s1QyFOZlhxOrY6gAC'
#                                            f'1NwxG5cCsEi77a-PhBv5pQAIAQADAgADeQAHHgQ')


def _get_userProfile_vip_handlers() -> tuple[MessageHandler, ...]:
    return (
        MessageHandler(__userName, filters=get_vip_filters('userName')),
        MessageHandler(userName, filters=get_vip_filters('nameshake')),
        MessageHandler(__importChat, filters=get_vip_filters('importchat')),
        # MessageHandler(__sendMsgById, filters=get_vip_filters('sendphoto')),
    )
