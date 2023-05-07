import os
import datetime
import time
from database import sync_db
from config import read_config
import importlib
from models.models import Message

config = read_config()


def onMessage(handler, callback):
    while True:
        write_ahead_file = config.get("database", "write_ahead_file")
        print("Monitoring {}".format(write_ahead_file))
        previous_last_modified = None
        total_messages = Message.select().count()
        while True:
            last_modified = os.stat(write_ahead_file).st_mtime
            if (
                previous_last_modified is not None
                and last_modified != previous_last_modified
            ):
                print("Database was modified")
                break
            else:
                print("No new messages were received")
            previous_last_modified = last_modified
            time.sleep(1)
        sync_db()
        if Message.select().count() > total_messages:
            print("New messages were received at {}".format(datetime.datetime.now()))
            module_name = f"events.onMessage.handlers.{handler}"
            module = importlib.import_module(module_name)
            handler_function = getattr(module, f"{handler}")
            handler_function(callback)
