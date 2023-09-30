from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message

# from user_bot.filters.main import get_vip_filters, textStartswith


async def __get_file_by_id(app: Client, msg: Message):
    to_userId = msg.chat.id
    user_info = await app.get_users(to_userId)

    msg_data = msg.text.split('|')
    msg_type = msg_data[0]
    file_id = msg_data[1]
    user = msg.from_user
    chat_id = 6120549837 #Bot chat

    if msg_type == 'photo':
        await app.send_photo(chat_id, file_id)
    elif msg_type == 'video':
        await app.send_photo(chat_id, file_id)
    elif msg_type == 'voice':
        await app.send_photo(chat_id, file_id)
    elif msg_type == 'video_note':
        await app.send_photo(chat_id, file_id)
    else:
        await app.send_message(chat_id, f'неизвестный файл: {file_id}')


# def _get_message_by_id() -> tuple[MessageHandler, ...]:
#     return (
#         MessageHandler(__get_file_by_id, filters=textStartswith('photo|')),
#         MessageHandler(__get_file_by_id, filters=textStartswith('video|')),
#         MessageHandler(__get_file_by_id, filters=textStartswith('voice|')),
#         MessageHandler(__get_file_by_id, filters=textStartswith('video_note|')),
#     )