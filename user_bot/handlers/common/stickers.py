from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message

from user_bot.filters import get_free_filters
from user_bot.utils import cmd, play_stroke_anim


@cmd()
async def __steve(app: Client, msg: Message):
    img = (
        "🏿🏿🏿🏿🏿🏿🏿🏿",
        "🏿🏿🏽🏽🏽🏽🏿🏿",
        "🏽🏽🏽🏽🏽🏽🏽🏽",
        "🏽⬜️⬛️🏽🏽⬛️⬜️🏽",
        "🏽🏽🏽🏿🏿🏽🏽🏽",
        "🏽🏽🏿🏽🏽🏿🏽🏽",
        "🏽🏽🏿🏿🏿🏿🏽🏽",
    )
    await play_stroke_anim(msg, img)


@cmd()
async def __gubka(app: Client, msg: Message):
    img = (
        "╲┏━┳━━━━━━━━┓╲╲",
        "╲┃◯┃╭┻┻╮╭┻┻╮┃╲╲",
        "╲┃╮┃┃╭╮┃┃╭╮┃┃╲╲",
        "╲┃╯┃┗┻┻┛┗┻┻┻┻╮╲",
        "╲┃◯┃╭╮╰╯┏━━━┳╯╲",
        "╲┃╭┃╰┏┳┳┳┳┓◯┃╲╲",
        "╲┃╰┃◯╰┗┛┗┛╯╭┃╲╲",
    )
    await play_stroke_anim(msg, img)


@cmd()
async def __dislike(app: Client, msg: Message):
    img = (
        "🟥🟥🟥🟥🟥🟥🟥🟥",
        "🟥🟥⬜️⬜️⬜️🟥⬜️🟥",
        "🟥🟥⬜️⬜️⬜️🟥⬜️🟥",
        "🟥⬜️⬜️⬜️⬜️🟥⬜️🟥",
        "🟥🟥🟥🟥⬜️🟥🟥🟥",
        "🟥🟥🟥🟥🟥🟥🟥🟥",
    )
    await play_stroke_anim(msg, img)


def _get_sticker_handlers() -> tuple[MessageHandler, ...]:
    return (
        MessageHandler(__steve, filters=get_free_filters('steve')),
        MessageHandler(__gubka, filters=get_free_filters('gubka')),
        MessageHandler(__dislike, filters=get_free_filters('dislike')),
    )
