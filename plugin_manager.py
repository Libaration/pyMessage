import inspect
import importlib
from plugins.baseplugin.baseplugin import BasePlugin
import os


class PluginManager:
    def __init__(self):
        self.plugins = []

    def register_plugin(self, plugin_cls):
        self.plugins.append(plugin_cls())

    def onMessageReceive(self, message):
        print("Message received")
        print("Plugins: ", self.plugins)
        print(self.plugins[0].event_handlers)
        for plugin in self.plugins:
            if "onMessageReceive" in plugin.event_handlers:
                plugin.event_handlers["onMessageReceive"](message)

    def load_plugins(self):
        plugin_dir = os.path.join(os.path.dirname(__file__), "plugins")
        for file_name in os.listdir(plugin_dir):
            if file_name.endswith(".py") and file_name != "__init__.py":
                module_name = file_name[:-3]
                module = importlib.import_module(f"plugins.{module_name}")
                for name, obj in inspect.getmembers(module):
                    if (
                        inspect.isclass(obj)
                        and issubclass(obj, BasePlugin)
                        and obj is not BasePlugin
                    ):
                        print(f"Registering plugin: {name}")
                        self.register_plugin(obj)
