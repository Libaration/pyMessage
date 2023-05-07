class BasePlugin:
    @staticmethod
    def register_plugin(cls):
        cls._is_plugin = True
        return cls

    def __init__(self, plugin_name, author, version, **kwargs):
        self.plugin_name = plugin_name
        self.author = author
        self.version = version
        self.event_handlers = {}
        self.register_event("onMessageReceive", self.onMessageReceive)
        self.initialize()

    def onMessageReceive(self, message):
        pass

    def register_event(self, event_name, handler):
        self.event_handlers[event_name] = handler

    def initialize(self):
        print(
            f"Plugin {self.plugin_name} by {self.author}, version {self.version} loaded"
        )
