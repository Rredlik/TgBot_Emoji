from asyncio import sleep
from random import choice

from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message

from misc.html_tags import b
from user_bot.filters import get_free_filters
from user_bot.handlers.common.games import _get_game_handlers
from user_bot.utils import cmd, play_anim
from user_bot.handlers.common.stickers import _get_sticker_handlers
from user_bot.handlers.common.texts import _get_text_handlers


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


@cmd(True)
async def __bombs(app: Client, msg: Message):
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


@cmd()
async def __compli(app: Client, msg: Message):
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


@cmd()
async def __voodoo(app: Client, msg: Message):
    strokes = (
        'Потомок звёздного семени, родом из вселенной',
        'Пепелю зелень, куплеты горячей кометы',
        'Метод имитации времени',
        'Так я ебу этих сук одновременно',
        'Держу баланс, я не держу балласт',
        'Ограняю алмаз, стержень не даст упасть',
        'Громкий боезапас, слово имеет власть',
        'Я кручу новый слайс, я курю это всласть',
        'Джо жирный, как Тоторо',
        'Я курю окорок,  раньше жил впроголодь',
        'Теперь я трачу в день не знаю сколько',
        'Дро крапалю на банкноты',
        'Кровь и пот, rollin’ up, блюдо подано',
        'Восемь лет опыта',
        'Бро, ты не собранный',
        'Время тратишь на задачи для робота',
        'Знание накоплено, молчание — золото',
        'До сих пор не верю, как вылез из омута',
        'Ищешь лекала в фекалиях',
        'Я уникален, на мне аномалии',
        'Мимо мигалок, лёгкое касание',
        'Взрываю здание, лайвы — пизда',
        'Мы наваливаем, при мне палево',
        'Пепелю пальмы, будто её задницу',
        'Вверх вертикально, я чувствую разницу',
        'Парень поднялся, сосункам на зависть',
        'Опускайте занавес, роллю тяжелый вес',
        'Мой флоу, как монумент; это — манна небес',
        'С майком наперевес, нахуй твой пресс',
        'Буду честным: дую больше, чем весь духовой оркестр',
        'Курю свиток кошачьей походки',
        'Мои парни — танки, ебут перепонки',
        'Самый прущий сканк, биток требует порки',
        'Но ты лишь обёртка, я клининг-уборка',
        'Ты понял',
        'Вуду (Эй), вуду(Эй), вуду(Эй), вуду(Эй)',
    )
    for stroke in strokes:
        await msg.edit(b(f'{stroke}'))
        await sleep(1.5)


def get_common_handlers() -> tuple[MessageHandler, ...]:
    return (
        MessageHandler(__bombs, filters=get_free_filters('bombs')),
        MessageHandler(__night, filters=get_free_filters('night')),
        MessageHandler(__stupid, filters=get_free_filters('stupid')),
        MessageHandler(__compli, filters=get_free_filters('compli')),
        MessageHandler(__voodoo, filters=get_free_filters('voodoo')),

        *_get_game_handlers(),
        *_get_text_handlers(),
        *_get_sticker_handlers(),
    )
