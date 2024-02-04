import os
from abc import ABC
from typing import Final
from environs import Env

from yookassa import Configuration


class Env(ABC):
    env = Env()
    env.read_env()
    ADMIN_ID: Final = env.int("ADMIN_ID")  # int(os.environ.get("ADMIN_ID", "define me!"))
    BOT_TOKEN: Final = env.str('BOT_TOKEN')  # , 'define me!')
    # PAYMENTS_TOKEN: Final = env.str("PAYMENTS_TOKEN")  # , "define me!")

    API_ID: Final = env.str("API_ID")  # , "define me!")
    API_HASH: Final = env.str("API_HASH")  # , "define me!")

    # SHOP_ID: Final = env.str("SHOP_ID")  # , "define me!")
    # SHOP_TOKEN: Final = env.str("SHOP_TOKEN")  # , "define me!")


# Configuration.configure(account_id=Env.SHOP_ID, secret_key=Env.SHOP_TOKEN)
