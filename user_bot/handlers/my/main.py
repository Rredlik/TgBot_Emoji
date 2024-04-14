from typing import Tuple, Any

import asyncio
from loguru import logger
from pyrogram import Client
from pyrogram.errors import exceptions
from pyrogram.handlers import MessageHandler, DeletedMessagesHandler
from pyrogram.types import Message, User

from telegram_bot.database.methods.create import new_message
from telegram_bot.database.methods.get import get_message_by_id
from telegram_bot.database.methods.update import mark_message_as_deleted
from user_bot.filters import msgFromMe
from user_bot.filters.main import msgToMe, privateChat, get_vip_filters, get_free_filters
# from user_bot.handlers.my.get_file_notWork import _get_message_by_id
from user_bot.utils.util import send_message_fromPyroToAio, cmd


async def __checkMyOutgoingMessages(app: Client, msg: Message):
    to_userId = msg.chat.id
    is_bot = msg.from_user.is_bot
    # user_info = await app.get_users(to_userId)

    if not is_bot:
        text, msg_id = await checkMessageType(app, msg)
        fromFirstName = msg.from_user.first_name if not None else msg.from_user.username
        toFirstName = msg.chat.first_name if not None else msg.chat.username
        my_id = msg.from_user.id
        # print('__checkMyOutgoingMessages', msg)
        # print('__checkMyOutgoingMessages', app)
        date = str(msg.date)
        new_message(chat_owner_id=my_id, date=date, from_user_id=my_id, to_user_id=to_userId,
                    message_text=text, message_id=msg_id)

        logger.info(f'{fromFirstName}({my_id}) -> {toFirstName}({to_userId}): {text}')


async def __checkMyIncomingMessages(app: Client, msg: Message):
    if not msg.from_user.is_bot:
        # print(msg)
        text, msg_id = await checkMessageType(app, msg)
        user = await get_me_antiFlood(app)
        # user_id = app.session
        # print('__checkMyIncomingMessages', msg)
        # print('__checkMyIncomingMessages', app)
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
    user = await get_me_antiFlood(app)
    # print(messages)
    for msg in messages:
        if msg.chat is None:
            mark_message_as_deleted(user.id, msg.id)
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


async def get_me_antiFlood(app: Client) -> User:

    try:
        # user_id = await app.session.user_id
        user = await app.get_me()
    except exceptions.FloodWait as e:
        # print("get_me_antiFlood:", e)
        # print("get_me_antiFlood:", e.value)
        logger.error(f"Flood limit is exceeded. Sleep {e.value} seconds.")
        await asyncio.sleep(e.value)
        user = await get_me_antiFlood(app)
        return user  # Recursive call
    except Exception as er:
        logger.error(f"{er}")
    else:
        return user


@cmd()
async def __checkNewOption(app: Client, msg: Message):
    # to_userId = msg.chat.id
    # is_bot = msg.from_user.is_bot
    # user_info = await app.get_users(to_userId)
    print('check')
    await app.send_cached_media(351931465,
                                'AgACAgIAAxkBAAED55Jlv_9DCOdRwEK3DJTOhaYxUdBzxQACHNQxG4cwAUqqX2TkI55jGgAIAQADAgADeQAHHgQ')


def get_my_handlers() -> tuple[MessageHandler, MessageHandler, DeletedMessagesHandler]:
    return (

        MessageHandler(__checkMyOutgoingMessages, filters=msgFromMe()),
        MessageHandler(__checkMyIncomingMessages, filters=msgToMe()),
        MessageHandler(__checkNewOption, filters=get_free_filters('checkoption')),
        DeletedMessagesHandler(__checkDeletingMessages),
        # *_get_message_by_id(),

    )
