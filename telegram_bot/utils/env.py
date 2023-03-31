import os
from abc import ABC
from typing import Final

from yookassa import Configuration


class Env(ABC):
    TOKEN: Final = os.environ.get('TOKEN', 'define me!')
    PAYMENTS_TOKEN: Final = os.environ.get("PAYMENTS_TOKEN", "define me!")
    API_ID: Final = os.environ.get("API_ID", "define me!")
    API_HASH: Final = os.environ.get("API_HASH", "define me!")
    ADMIN_ID: Final = int(os.environ.get("ADMIN_ID", "define me!"))
    SHOP_ID: Final = os.environ.get("SHOP_ID", "define me!")
    SHOP_TOKEN: Final = os.environ.get("SHOP_TOKEN", "define me!")


Configuration.configure(account_id=Env.SHOP_ID, secret_key=Env.SHOP_TOKEN)