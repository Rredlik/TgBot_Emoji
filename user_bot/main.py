import logging
import sys
from pyrogram import Client
from user_bot.handlers import register_all_handlers


def start_user_bot() -> None:
    string_session = sys.argv[1]
    telegram_id = sys.argv[2]
    # logging.basicConfig(format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    #                     level=logging.DEBUG)
    # logger = logging.getLogger(__name__)
    client = Client(
        name=telegram_id,
        session_string=string_session,
        in_memory=True,
        device_model='Redmi Note 11S'
        # app_version='10.1.0',
    )
    register_all_handlers(client)
    client.run()
