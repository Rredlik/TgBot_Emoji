from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message

from user_bot.filters import get_free_filters
from user_bot.handlers.common.games import _get_game_handlers
from user_bot.handlers.common.stickers import _get_sticker_handlers
from user_bot.handlers.common.texts import _get_text_handlers
from user_bot.utils import cmd, play_anim


@cmd(True)
async def __stupid(app: Client, msg: Message):
    first_str = 'YOUR BRAIN ➡️ 🧠\n\n🧠'
    second_str = 'YOUR BRAIN ➡️ 🧠\n\n'
    words = (
        f'{first_str}         (^_^)🗑',
        f'{first_str}       (^_^)  🗑',
        f'{first_str}     (^_^)    🗑',
        f'{first_str}   (^_^)      🗑',
        f'{first_str} (^_^)        🗑',
        f'{first_str} <(^_^ <)     🗑',
        f'{second_str}(> ^_^)>🧠   🗑',
        f'{second_str} (> ^_^)>🧠  🗑',
        f'{second_str}  (> ^_^)>🧠 🗑',
        f'{second_str}   (> ^_^)>🧠🗑',
        f'{second_str}       (^_^) 🗑',
        f'{second_str}        (3_3)🗑'
    )
    await play_anim(msg, words)


@cmd(True)
async def __bombs(app, msg: Message):
    row = '▪️▪️▪️▪️\n'
    bombs = '💣 💣 💣 💣\n'
    fire = '💥 💥 💥 💥\n'
    smile = '😵 😵 😵 😵\n'
    words = (
        f"{row}{row}{row}{row}{row}",
        f"{bombs}{row}{row}{row}{row}",
        f"{row}{bombs}{row}{row}{row}",
        f"{row}{row}{bombs}{row}{row}",
        f"{row}{row}{row}{bombs}{row}",
        f"{row}{row}{row}{row}{bombs}",
        f"{row}{row}{row}{row}{fire}",
        f"{row}{row}{row}{fire}{fire}",
        f"{row}{row}{row}{row}{smile}"
    )
    await play_anim(msg, words)


def get_common_handlers() -> tuple[MessageHandler, ...]:
    return (
        MessageHandler(__stupid, filters=get_free_filters('stupid')),
        MessageHandler(__bombs, filters=get_free_filters('bombs')),

        *_get_game_handlers(),
        *_get_text_handlers(),
        *_get_sticker_handlers(),
    )
