import os
import colorama
from events import onMessage
from config import read_config
from models.models import *

config = read_config()


def main():
    def callback(last_message):
        print("Last message: {}".format(last_message))

    onMessage("receive", callback)


if __name__ == "__main__":
    connect()
    main()
