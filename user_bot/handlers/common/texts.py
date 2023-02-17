from random import choice

from asyncio import sleep

from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message

from misc.html_tags import b
from user_bot.filters import get_free_filters
from user_bot.utils import cmd, play_stroke_anim


@cmd()
async def __hello(app: Client, msg: Message):
    text = (
        "╔┓┏╦━━╦┓╔┓╔━━╗",
        "║┗┛║┗━╣┃║┃║╯╰║",
        "║┏┓║┏━╣┗╣┗╣╰╯║",
        "╚┛┗╩━━╩━╩━╩━━╝"
    )
    await play_stroke_anim(msg, text)


@cmd()
async def __press_f(app: Client, msg: Message):
    text = (
        "████████",
        "██",
        "██",
        "██████",
        "██",
        "██",
        "██"
    )
    await play_stroke_anim(msg, text)


@cmd()
async def __lol(app: Client, msg: Message):
    text = (
        "┏━┓┈┈╭━━━━╮┏━┓┈┈",
        "┃╱┃┈┈┃╱╭╮╱┃┃╱┃┈┈",
        "┃╱┗━┓┃╱┃┃╱┃┃╱┗━┓",
        "┃╱╱╱┃┃╱╰╯╱┃┃╱╱╱┃",
        "┗━━━┛╰━━━━╯┗━━━┛",
    )
    await play_stroke_anim(msg, text)


@cmd()
async def __battle(app: Client, msg: Message):
    words = (
        'говно', 'залупа', 'пенис', 'хер', 'давалка', 'хуй', 'блядина',
        'головка', 'шлюха', 'жопа', 'член', 'еблан', 'петух', 'мудила',
        'рукоблуд', 'ссанина', 'очко', 'блядун', 'вагина',
        'сука', 'ебланище', 'влагалище', 'пердун', 'дрочила',
        'пидор', 'пизда', 'туз', 'малафья', 'гомик', 'мудила', 'пилотка', 'манда',
        'анус', 'вагина', 'путана', 'педрила', 'шалава', 'хуила', 'мошонка', 'елда'
    )
    for word in words:
        await msg.edit(b(f'{word}'))
        await sleep(0.5)
    await msg.edit(b(f'Ты {choice(words)}✨'))

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


def _get_text_handlers() -> tuple[MessageHandler, ...]:
    return (
        MessageHandler(__hello, filters=get_free_filters('hello')),
        MessageHandler(__press_f, filters=get_free_filters('f')),
        MessageHandler(__lol, filters=get_free_filters('lol')),
        MessageHandler(__voodoo, filters=get_free_filters('voodoo')),
        MessageHandler(__battle, filters=get_free_filters('battle')),
    )
