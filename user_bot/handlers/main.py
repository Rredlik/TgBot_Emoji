from pyrogram import Client

from user_bot.handlers.my import get_my_handlers
from user_bot.handlers.vip import get_vip_handlers
from user_bot.handlers.common import get_common_handlers


def register_all_handlers(client: Client) -> None:
    handlers = (
        *get_common_handlers(),
        *get_vip_handlers(),
        *get_my_handlers(),
    )
    for handler in handlers:
        client.add_handler(handler)
