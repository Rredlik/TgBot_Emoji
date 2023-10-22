from aiogram import Dispatcher, Bot
from aiogram.types import Message


async def __get_file_by_id(msg: Message) -> None:
    bot: Bot = msg.bot
    msg_data = msg.text.split('|')
    msg_type = msg_data[0]
    file_id = msg_data[1]
    user = msg.from_user
    file_path = 'downloads'

    if msg_type == 'photo':
        await bot.send_photo(user.id, open(f"{file_path}/{file_id}.jpg", "rb"))
    elif msg_type == 'video':
        await bot.send_video(user.id, open(f"{file_path}/{file_id}.mp4", "rb"))
    elif msg_type == 'voice':
        await bot.send_voice(user.id, open(f"{file_path}/{file_id}.ogg", "rb"))
    elif msg_type == 'video_note':
        await bot.send_video_note(user.id, open(f"{file_path}/{file_id}.mp4", "rb"))
    elif msg_type.startswith('document_'):
        file_type = msg_type.split('_')[1]
        await bot.send_document(user.id, open(f"{file_path}/{file_id}.{file_type}", "rb"))
    else:
        await bot.send_message(user.id, f'неизвестный файл: {file_id}')


def _get_my_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(__get_file_by_id, content_types=['text'], text_contains="photo|")
    dp.register_message_handler(__get_file_by_id, content_types=['text'], text_contains="video|")
    dp.register_message_handler(__get_file_by_id, content_types=['text'], text_contains="voice|")
    dp.register_message_handler(__get_file_by_id, content_types=['text'], text_contains="video_note|")
    dp.register_message_handler(__get_file_by_id, content_types=['text'], text_contains="document_")
