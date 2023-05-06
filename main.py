import os
import colorama
from database import monitorMessages
from config import read_config
from models.models import *

config = read_config()


def main():
    path = config.get("database", "path")
    write_ahead_file = "chat.db-wal"
    messages_db_file = os.path.join(path, write_ahead_file)
    monitorMessages(messages_db_file)
    last_message = Message.get_last_message().text
    print("Last message: {}".format(last_message))
    return last_message


if __name__ == "__main__":
    connect()
    main()
