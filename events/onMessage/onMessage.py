import os
import datetime
import time
from database import sync_db
from config import read_config
import importlib

config = read_config()


def onMessage(trigger_type, callback):
    write_ahead_file = config.get("database", "write_ahead_file")
    print("Monitoring {}".format(write_ahead_file))
    previous_last_modified = None
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
    print("New messages were received at {}".format(datetime.datetime.now()))
    module_name = f"events.onMessage.triggers.{trigger_type}"
    module = importlib.import_module(module_name)
    trigger_function = getattr(module, f"{trigger_type}")
    trigger_function(callback)
