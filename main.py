import os
import configparser
import colorama
from database import monitorMessages, getLastMessage
from config import read_config
from models.models import connect

config = read_config()


def main():
    path = config.get("database", "path")
    write_ahead_file = "chat.db-wal"
    messages_db_file = os.path.join(path, write_ahead_file)
    monitorMessages(messages_db_file)
    last_message = getLastMessage(config.get("database", "db_file"))
    print("Last message: {}".format(last_message))
    return last_message


def read_config():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config


if __name__ == "__main__":
    connect()
    main()
