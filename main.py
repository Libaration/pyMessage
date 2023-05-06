import os
import colorama
from events import onMessage
from config import read_config
from models.models import *
from plugin_manager import PluginManager

config = read_config()


def main():
    def callback(last_message):
        print("Last message: {}".format(last_message))

    # onMessage("receive", callback)


if __name__ == "__main__":
    # connect()
    plugin_manager = PluginManager()
    plugin_manager.load_plugins()
    main()
