from contextlib import suppress

from aiogram import Dispatcher, executor
from aiogram.utils.exceptions import ChatNotFound, BotBlocked
from loguru import logger

from loader import dp
from telegram_bot.database import register_models
from telegram_bot.database.methods.get import get_users_with_sessions
from telegram_bot.filters import register_all_filters
from telegram_bot.handlers import register_all_handlers
from telegram_bot.keyboards import get_main_keyboard
from telegram_bot.utils.process import start_process_if_sessions_exists


async def __on_start_up(dp: Dispatcher) -> None:
    logger.info('Bot starts')

    register_models()
    register_all_filters(dp)
    register_all_handlers(dp)

    users = get_users_with_sessions()
    count = 0

    if not users:
        return
    await dp.bot.send_message(351931465, "Бот запущен!",
                              reply_markup=get_main_keyboard(351931465))
    for user in users:
        with suppress(ChatNotFound, BotBlocked):
            if user.session.enable:
                start_process_if_sessions_exists(user.telegram_id)
                count += 1
            # if user.telegram_id == '351931465':
            #     # await dp.bot.send_message(user.telegram_id, "Бот обновлен!",
            #     #                           reply_markup=get_main_keyboard(user.telegram_id))
            #     print('admin')

    logger.info(f"Было запущенно {count} аккаунтов")


def start_telegram_bot() -> None:
    # logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    #                     level=logging.DEBUG)
    # logger = logging.getLogger(__name__)
    # dp = get_Dispatcher()
    executor.start_polling(dp, skip_updates=True, on_startup=__on_start_up)
