from random import randint, choice

from asyncio import sleep

from pyrogram import Client
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler

from user_bot.filters import get_vip_filters
from user_bot.handlers.vip.util import _get_heart_stickers
from user_bot.utils import play_stroke_anim, cmd


@cmd()
async def __rabbit(app: Client, msg: Message):
    left_eyes = '┈┃▋▏▋▏┃┈'
    right_eyes = '┈┃╱▋╱▋┃┈'
    img = [
        '╭━━╮╭━━╮',
        '╰━╮┃┃╭━╯',
        '┈╭┛┗┛┗╮┈',
        '┈┃╱▋╱▋┃┈',
        '╭┛▔▃▔┈┗╮',
        '╰┓╰┻━╯┏╯',
        '╭┛┈┏┓┈┗╮',
        '╰━━╯╰━━╯',
    ]
    eyes = choice((True, False))
    img[3] = right_eyes if eyes else left_eyes
    await play_stroke_anim(msg, img)
    await sleep(1)

    for _ in range(randint(10, 20)):
        eyes = not eyes
        img[3] = right_eyes if eyes else left_eyes
        await msg.edit('\n'.join(img))
        await sleep(0.5)


@cmd()
async def __like(app: Client, msg: Message):
    img = (
        "🟦🟦🟦🟦🟦🟦🟦🟦",
        "🟦🟦🟦🟦⬜️🟦🟦🟦",
        "🟦🟦⬜️⬜️⬜️🟦⬜️🟦",
        "🟦🟦⬜️⬜️⬜️🟦⬜️🟦",
        "🟦🟦⬜️⬜️⬜️🟦⬜️🟦",
        "🟦🟦🟦🟦🟦🟦🟦🟦",
    )
    await play_stroke_anim(msg, img)


@cmd()
async def __heart(app: Client, msg: Message):
    img = _get_heart_stickers()
    for anim in img:
        await msg.edit('\n'.join(anim))
        await sleep(0.5)


@cmd()
async def __uno(app: Client, msg: Message):
    img = (
        "⣿⣿⣿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇",
        "⣿⣿⡟⡴⠛⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇",
        "⣿⡏⠴⠞⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇",
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇",
        "⣿⣿⣿⣿⣿⣿⣿⡏⠩⣭⣭⢹⣿⣿⣿⣿⡇",
        "⣿⣿⣿⣿⣿⣿⠟⣵⣾⠟⠟⣼⣿⣿⣿⣿⡇",
        "⣿⣿⣿⣿⣿⠿⠀⢛⣵⡆⣶⣿⣿⣿⣿⣿⡇",
        "⣿⣿⣿⣿⡏⢸⣶⡿⢋⣴⣿⣿⣿⣿⣿⣿⡇",
        "⣿⣿⣿⣿⣇⣈⣉⣉⣼⣿⣿⣿⣿⣿⣿⣿⡇",
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇",
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢣⠞⢺⣿⡇",
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢡⡴⣣⣿⣿⡇",
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿⡇"
    )
    await play_stroke_anim(msg, img)


def _get_sticker_vip_handlers() -> tuple[MessageHandler, ...]:
    return (
        MessageHandler(__like, filters=get_vip_filters('like')),
        MessageHandler(__heart, filters=get_vip_filters('heart')),
        MessageHandler(__rabbit, filters=get_vip_filters('rabbit')),
        MessageHandler(__uno, filters=get_vip_filters('uno')),
    )
