from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message

from user_bot.filters import msgFromMe
from user_bot.filters.main import msgToMe


async def __checkMyOutgoingMessages(app: Client, msg: Message):

    fromFirstName = msg.from_user.first_name if not None else msg.from_user.username
    toFirstName = msg.chat.first_name if not None else msg.chat.username
    print(f'{msg.date} {fromFirstName}(Me) -> {toFirstName}({msg.chat.id}): {msg.text}')


async def __checkMyIncomingMessages(app: Client, msg: Message):
    # session = app.
    fromFirstName = msg.from_user.first_name if not None else msg.from_user.username
    # toFirstName = msg.chat.first_name if not None else msg.chat.username
    # print(session)
    print(f'{msg.date} {fromFirstName}({msg.from_user.id}) -> Me(): {msg.text}')


def get_my_handlers() -> tuple[MessageHandler, ...]:
    return (
        MessageHandler(__checkMyOutgoingMessages, filters=msgFromMe()),
        MessageHandler(__checkMyIncomingMessages, filters=msgToMe()),
    )