import sqlalchemy.exc

from telegram_bot.database.main import Database
from telegram_bot.database.methods.get import get_user_by_telegram_id
from telegram_bot.database.models import User, Session, Payment, Message


def create_user(telegram_id: int) -> None:
    session = Database().session
    try:
        session.query(User.telegram_id).filter(User.telegram_id == telegram_id).one()
    except sqlalchemy.exc.NoResultFound:
        session.add(User(telegram_id=telegram_id))
        session.commit()



def create_session(user: User, user_bot_session: str) -> None:
    session = Database().session
    session.add(Session(user_id=user.id, string=user_bot_session))
    session.commit()


def create_user_payment(user: User, key) -> None:
    session = Database().session
    session.add(Payment(user_id=user.id, key=key))
    session.commit()


def new_message(chat_owner_id, date, from_user_id, to_user_id, message_text, message_id) -> None:
    session = Database().session

    try:
        session.query(Message.message_id).filter(Message.message_id == message_id).one()
    except sqlalchemy.exc.NoResultFound:
        chat_owner = get_user_by_telegram_id(chat_owner_id)
        session.add(Message(chat_owner=chat_owner.telegram_id, date=date, from_user_id=from_user_id, to_user_id=to_user_id,
                            message_text=message_text, message_id=message_id))
        session.commit()
