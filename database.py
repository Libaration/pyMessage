import datetime
import time
import os


def monitorMessages(messages_db_file):
    print("Monitoring {}".format(messages_db_file))
    previous_last_modified = None
    while True:
        last_modified = os.stat(messages_db_file).st_mtime
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
