import datetime
import time
import os
import sqlite3
from config import read_config
from peewee import *
from models.models import *
import pdb


def monitorMessages(write_ahead_file):
    pdb.set_trace()
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
    print("New messages were received at {}".format(datetime.datetime.now()))


def getLastMessage(messages_db_file):
    conn = sqlite3.connect(messages_db_file)
    query = "SELECT text from message ORDER BY ROWID DESC"
    cursor = conn.cursor()
    last_message = cursor.execute(query).fetchone()
    return last_message[0]
