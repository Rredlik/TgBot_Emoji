from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import Env
# import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config.env import Env

bot = Bot(token=Env.BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())

def get_Bot():
    bot = Bot(token=Env.BOT_TOKEN, parse_mode='HTML')
    return bot


# def get_Dispatcher():
#     bot = get_Bot()
#     dp = Dispatcher(bot, storage=MemoryStorage())
#     return dp
