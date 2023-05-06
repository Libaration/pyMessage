class BasePlugin:
    @staticmethod
    def register_plugin(cls):
        cls._is_plugin = True
        return cls

    def __init__(self, plugin_name, author, version):
        self.plugin_name = plugin_name
        self.author = author
        self.version = version
        self.initialize()

    def initialize(self):
        print(
            f"Plugin {self.plugin_name} by {self.author}, version {self.version} loaded"
        )
