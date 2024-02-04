from typing import Tuple, Any

from loguru import logger
from pyrogram import Client
from pyrogram.handlers import MessageHandler, DeletedMessagesHandler
from pyrogram.types import Message

from telegram_bot.database.methods.create import new_message
from telegram_bot.database.methods.get import get_message_by_id
from telegram_bot.database.methods.update import delete_message
from user_bot.filters import msgFromMe
from user_bot.filters.main import msgToMe, privateChat
# from user_bot.handlers.my.get_file_notWork import _get_message_by_id
from user_bot.utils.util import send_message_fromPyroToAio


async def __checkMyOutgoingMessages(app: Client, msg: Message):
    to_userId = msg.chat.id
    is_bot = msg.from_user.is_bot
    # user_info = await app.get_users(to_userId)

    if not is_bot:
        text, msg_id = await checkMessageType(app, msg)
        fromFirstName = msg.from_user.first_name if not None else msg.from_user.username
        toFirstName = msg.chat.first_name if not None else msg.chat.username
        my_id = (await app.get_me()).id
        date = str(msg.date)
        new_message(chat_owner_id=my_id, date=date, from_user_id=my_id, to_user_id=to_userId,
                    message_text=text, message_id=msg_id)

        logger.info(f'{fromFirstName}({my_id}) -> {toFirstName}({to_userId}): {text}')


async def __checkMyIncomingMessages(app: Client, msg: Message):
    if not msg.from_user.is_bot:
        # print(msg)
        text, msg_id = await checkMessageType(app, msg)
        user = await app.get_me()
        fromFirstName = msg.from_user.first_name if not None else msg.from_user.username
        toFirstName = user.first_name if not None else user.username

        fromUser_id = int(msg.from_user.id)
        date = str(msg.date)
        new_message(chat_owner_id=user.id, date=date, from_user_id=fromUser_id, to_user_id=user.id,
                    message_text=text, message_id=msg_id)
        logger.info(f'{fromFirstName}({fromUser_id}) -> {toFirstName}({user.id}): {text}')


async def __checkDeletingMessages(app: Client, messages):

    for msg in messages:
        if msg.chat is not None:
            messages.remove(msg)

    if len(messages) == 0:
        return
    user = await app.get_me()
    # print(messages)
    for msg in messages:
        if msg.chat is None:
            delete_message(user.id, msg.id)
            message = get_message_by_id(msg.id)

            if message is not None:
                users = await app.get_users([message.from_user_id, message.to_user_id])
                from_user = users[0]
                if message.from_user_id != message.to_user_id:
                    to_user = users[1]
                else:
                    to_user = users[0]

                log_text = f'❌ Удаление сообщения | @{from_user.username} (from_user.id) -> @{to_user.username} ' \
                           f'(to_user.id) | {message.date} | ' \
                           f'{message.message_text} '
                logger.info(log_text)
                msg_text = f'❌ Удаление сообщения\n' \
                           f'@{from_user.username} -> @{to_user.username}\n' \
                           f'{message.date}\n' \
                           f'<code>{message.message_text}</code>'
                await send_message_fromPyroToAio(351931465, msg_text)
        else:
            print(f'channel delete: {user.id} - {msg.chat.id} - {msg.id}')


async def checkMessageType(app, msg):
    size_const = 30  ##MB мегабайт
    msg_id = msg.id
    if msg.text is not None:
        text = msg.text

    elif msg.photo is not None:
        # print(msg.photo)
        file_id = msg.photo.file_id
        await app.download_media(file_id, f'{file_id}.jpg')
        text = f'photo|{file_id}|{msg.caption}'

    elif msg.video is not None:
        file_id = msg.video.file_id

        text = f'video|{file_id}|{msg.caption}'
        if msg.video.file_size < size_const*1024*1024:
            await app.download_media(file_id, f'{file_id}.mp4')
        else:
            text += f'video|{round(msg.video.file_size / 1024 / 1024, 1)} Mb > {size_const} Mb'

    elif msg.voice is not None:
        file_id = msg.voice.file_id
        await app.download_media(file_id, f'{file_id}.ogg')
        text = f'voice|{file_id}'

    elif msg.video_note is not None:
        file_id = msg.video_note.file_id
        await app.download_media(file_id, f'{file_id}.mp4')
        text = f'video_note|{file_id}'

    elif msg.sticker is not None:
        text = f'sticker|{msg.sticker.file_id}|{msg.sticker.emoji}'

    elif msg.document is not None:
        file_id = msg.document.file_id
        file_type = msg.document.file_name.split('.')[-1]

        text = f'document_{file_type}|{file_id}|{msg.caption}'
        if msg.document.file_size < size_const*1024*1024:
            await app.download_media(file_id, f'{file_id}.{file_type}')
        else:
            text += f'document_{file_type}|{round(msg.document.file_size / 1024 / 1024, 1)} Mb > {size_const} Mb'

    else:
        text = 'Неизвестный тип сообщения:\n' \
               f'{msg}'

    # print(text)
    return text, msg_id


def get_my_handlers() -> tuple[MessageHandler, MessageHandler, DeletedMessagesHandler]:
    return (

        MessageHandler(__checkMyOutgoingMessages, filters=msgFromMe()),
        MessageHandler(__checkMyIncomingMessages, filters=msgToMe()),
        DeletedMessagesHandler(__checkDeletingMessages),
        # *_get_message_by_id(),

    )
