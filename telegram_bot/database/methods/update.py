from telegram_bot.database.main import Database
from telegram_bot.database.methods.get import get_user_by_telegram_id
from telegram_bot.database.models import User, Message


def set_vip(telegram_id: int) -> None:
    Database().session.query(User).filter(User.telegram_id == telegram_id).update(values={User.vip: 1})
    Database().session.commit()


def set_admin(telegram_id: int) -> None:
    Database().session.query(User).filter(User.telegram_id == telegram_id).update(values={User.admin: 1})
    Database().session.commit()



def switch_is_userBotEnable(telegram_id: int, mode: int) -> None:
    Database().session.query(User).filter(User.telegram_id == telegram_id).update(values={User.is_enable: mode})
    Database().session.commit()


def update_session_status(telegram_id, enable) -> None:
    user = get_user_by_telegram_id(telegram_id)
    if user and user.session:
        user.session.enable = int(enable)
    Database().session.commit()


def mark_message_as_deleted(chat_owner_id, message_id) -> None:
    Database().session.query(Message).filter(Message.message_id == message_id and
                                             Message.chat_owner == chat_owner_id)\
        .update(values={Message.is_deleted: 1})
    Database().session.commit()


def update_message(chat_owner_id, message_text, message_id) -> bool:
    Database().session.query(Message).filter(Message.message_id == message_id and
                                             Message.chat_owner == chat_owner_id)\
        .update(values={Message.message_text: message_text})
    Database().session.commit()
    return True
