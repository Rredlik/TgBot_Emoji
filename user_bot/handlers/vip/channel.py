import asyncio

from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message

from user_bot.filters import get_vip_filters
from user_bot.utils import cmd


@cmd()
async def __channelName(app: Client, msg: Message):
    # userName = app.user
    asyncio.get_event_loop().run_until_complete(asyncio.ensure_future(channelName(app, msg)))


async def channelName(app: Client, msg: Message):
    strokes = (
        "👾ачо? а ничо!🦄",
        "ачо?👾а ничо!",
        "🦄ачо? а ничо!👾",
        "ачо? а🦄ничо!",
        "👾ачо? а ничо!🦄",
        "ачо? а👾ничо!",
        "🦄ачо? а ничо!👾",
        "ачо? 🦄а ничо!",
    )
    await msg.delete()

    # for i in range(1000):
    for stroke in strokes:
        await asyncio.sleep(2)
        channelname = await app.set_chat_title(chat_id=-1001665320015, title=stroke)
        print(channelname)


def _get_channel_vip_handlers() -> tuple[MessageHandler, ...]:
    return (
        MessageHandler(__channelName, filters=get_vip_filters('channelname')),
    )