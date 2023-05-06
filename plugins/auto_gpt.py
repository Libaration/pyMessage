from plugins.baseplugin import BasePlugin


@BasePlugin.register_plugin
class AutoGPT(BasePlugin):
    def __init__(self):
        super().__init__("AutoGPT", "Libaration", "0.0.1")
