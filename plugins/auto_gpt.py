from plugins.baseplugin import BasePlugin


@BasePlugin.register_plugin
class AutoGPT(BasePlugin):
    def __init__(self):
        super().__init__(plugin_name="AutoGPT", author="Libaration", version="0.0.1")

    def onMessageReceive(self, message):
        print("overriding onMessageReceive in AutoGPT plugin")
        print("Message: ", message)
