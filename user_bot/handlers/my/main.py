from typing import Tuple

from loguru import logger
from pyrogram import Client
from pyrogram.handlers import MessageHandler, DeletedMessagesHandler
from pyrogram.types import Message

from telegram_bot.database.methods.create import new_message
from telegram_bot.database.methods.get import get_message_by_id
from telegram_bot.database.methods.update import delete_message
from user_bot.filters import msgFromMe
from user_bot.filters.main import msgToMe


async def __checkMyOutgoingMessages(app: Client, msg: Message):
    to_userId = msg.chat.id
    user_info = await app.get_users(to_userId)

    if not user_info.is_bot:
        text, msg_id = await checkMessageType(msg)

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
        text, msg_id = await checkMessageType(msg)
        user = await app.get_me()
        fromFirstName = msg.from_user.first_name if not None else msg.from_user.username
        toFirstName = user.first_name if not None else user.username

        fromUser_id = int(msg.from_user.id)
        date = str(msg.date)
        new_message(chat_owner_id=user.id, date=date, from_user_id=fromUser_id, to_user_id=user.id,
                    message_text=text, message_id=msg_id)
        logger.info(f'{fromFirstName}({fromUser_id}) -> {toFirstName}({user.id}): {text}')


async def __checkDeletingMessages(app: Client, messages):
    user = await app.get_me()
    # print(messages)
    for msg in messages:
        if msg.chat is None:
            delete_message(user.id, msg.id)
            message = get_message_by_id(msg.id)
            logger.info(f'Удаление сообщения | {message.from_user_id} -> {message.to_user_id}: '
                        f'{message.message_text} | {message.date}')
        else:
            print(f'channel delete: {user.id} - {msg.chat.id} - {msg.id}')


        # below_message = await app.get_messages(1241977405, [5801, 5803, 19946, 19948, 23695, 23697, 29287, 29289])
        # print(below_message)
        # below_message = await app.get_messages(msg.id-1)
        # next_message = await app.get_messages(msg.id+1)
        # print(below_message, next_message)

        # below_message = await app.get_messages(5802 - 1)
        # next_message = await app.get_messages(5802 + 1)
        # print(below_message, next_message)
        #
        # below_message = await app.get_messages(19947 - 1)
        # next_message = await app.get_messages(19947 + 1)
        # print(below_message, next_message)


# No argument supplied. Either pass message_ids or reply_to_message_ids
# Traceback (most recent call last):
#   File "D:\Programming\Python_Projects\EmojiBotTG\venv\lib\site-packages\pyrogram\dispatcher.py", line 240, in handler_worker
#     await handler.callback(self.client, *args)
#   File "D:\Programming\Python_Projects\EmojiBotTG\user_bot\handlers\my\main.py", line 53, in __checkDeletingMessages
#     below_message = await app.get_messages(msg.id-1)
#   File "D:\Programming\Python_Projects\EmojiBotTG\venv\lib\site-packages\pyrogram\methods\messages\get_messages.py", line 97, in get_messages
#     raise ValueError("No argument supplied. Either pass message_ids or reply_to_message_ids")
# ValueError: No argument supplied. Either pass message_ids or reply_to_message_ids


#5802   19947   23696
async def checkMessageType(msg):
    msg_id = msg.id
    if msg.text is not None:
        text = msg.text
    elif msg.photo is not None:
        text = f'photo|{msg.photo.file_id}|{msg.caption}'
    elif msg.video is not None:
        text = f'video|{msg.video.file_id}|{msg.caption}'
    elif msg.voice is not None:
        text = f'voice|{msg.voice.file_id}'
    elif msg.video_note is not None:
        text = f'video_note|{msg.video_note.file_id}'
    else:
        text = None

    # print(text)
    return text, msg_id


def get_my_handlers() -> tuple[MessageHandler, MessageHandler, DeletedMessagesHandler]:
    return (
        MessageHandler(__checkMyOutgoingMessages, filters=msgFromMe()),
        MessageHandler(__checkMyIncomingMessages, filters=msgToMe()),
        DeletedMessagesHandler(__checkDeletingMessages)
    )
