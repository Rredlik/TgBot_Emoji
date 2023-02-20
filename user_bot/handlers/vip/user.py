import asyncio

from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message

from user_bot.filters import get_vip_filters
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


def _get_userProfile_vip_handlers() -> tuple[MessageHandler, ...]:
    return (
        MessageHandler(__userName, filters=get_vip_filters('userName')),
    )