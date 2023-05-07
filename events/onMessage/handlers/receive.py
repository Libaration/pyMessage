from database import sync_db
from config import read_config
from models.models import Message

config = read_config()


def receive(callback):
    last_message = Message.get_last_message().text
    callback(last_message)
