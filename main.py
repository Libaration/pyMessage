import os
import configparser
from database import monitorMessages

config = configparser.ConfigParser()
config.read("config.ini")


def main():
    path = config.get("database", "path")
    filename = "chat.db-wal"
    messages_db_file = os.path.join(path, filename)
    monitorMessages(messages_db_file)
    print("Outside the loop !")


if __name__ == "__main__":
    main()
