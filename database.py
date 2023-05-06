import datetime
import time
import os
from config import read_config
from peewee import *
from models.models import *
import pdb
import subprocess
from config import read_config


def sync_db():
    path = config.get("database", "path")
    db_copy_path = config.get("database", "db_copy_path")
    subprocess.run(["bash", "./scripts/resync.command", path, db_copy_path])
    print("Syncing database")
    time.sleep(1)
    print("Database synced")


def monitorMessages(write_ahead_file):
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
