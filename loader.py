from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import Env


def get_Bot():
    bot = Bot(token=Env.TOKEN, parse_mode='HTML')
    return bot


def get_Dispatcher():
    bot = get_Bot()
    dp = Dispatcher(bot, storage=MemoryStorage())
    return dp
