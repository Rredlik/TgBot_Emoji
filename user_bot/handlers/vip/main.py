from random import choice

from asyncio import sleep
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler

from misc.html_tags import b
from user_bot.filters.main import get_vip_filters
from user_bot.utils import UserConfig, cmd, play_anim
from user_bot.handlers.vip.games import _get_game_vip_handlers
from user_bot.handlers.vip.texts import _get_text_vip_handlers
from user_bot.handlers.vip.stickers import _get_sticker_vip_handlers


@cmd()
async def __bagger_fast(app, msg: Message):
    text = ''
    total = 'Pythоn ИМБА, Pythоn ЕДИН. И SKIDIKIS непобедим!!!'
    for char in total:
        text += char
        if char == ' ':
            continue
        await msg.edit(b(text))
        await sleep(0.1)


@cmd()
async def __night(app, msg: Message):
    sleep_words = (
        'зайка 💚', 'солнышко 💛', 'котёнок ❤', 'цветочек 💙', 'ангелочек 💜', 'принцесса 💓',
        'красотка 💕', 'милашка 💖', 'симпатяжка 💗', 'бусинка 💘',
    )
    love_words = (
        '❤ я ❤', '💚 тебя 💚', '💙 очень 💙', '💛 сильно 💛', '💜 люблю 💜',
    )
    for word in sleep_words:
        await msg.edit(b(f'Cпокойной ночи {word}'))
        await sleep(0.5)
    for word in love_words:
        await msg.edit(b(word))
        await sleep(0.5)


@cmd()
async def __compli(app, msg: Message):
    words = (
        'удивительная', 'внимательная', 'красивая', 'лучшая', 'успешная', 'заботливая', 'милая', 'прекрасная',
        'умная', 'шикарная', 'обалденная', 'очаровашка', 'любимая', 'весёлая', 'нежная', 'яркая', 'прелестная',
        'приятная', 'сладкая', 'дивная', 'ангельская', 'добрая', 'бесподобная', 'волшебная', 'крутышка', 'смелая',
        'ласковая', 'романтичная', 'великолепная', 'внимательная', 'страстная', 'игривая', 'единственная',
        'стройная', 'безумная', 'симпатичная', 'изящная', 'талантливая', 'элегантная', 'чуткая', 'уникальная',
    )
    await msg.edit('<b>Крошечные напоминания того, что ты...</b>')
    await sleep(1)

    for word in words:
        await msg.edit(b(f'Cамая {word}✨'))
        await sleep(0.5)
    await msg.edit(b(f'Cамая {choice(words)}✨'))


def get_vip_handlers() -> tuple | tuple[MessageHandler]:
    if not UserConfig.VIP_STATUS:
        return ()
    return (
        MessageHandler(__bagger_fast, filters=get_vip_filters('bf')),
        MessageHandler(__night, filters=get_vip_filters('night')),
        MessageHandler(__compli, filters=get_vip_filters('compli')),

        *_get_game_vip_handlers(),
        *_get_text_vip_handlers(),
        *_get_sticker_vip_handlers(),

    )
