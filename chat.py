class Chat(object):
    def __init__(self, name, users, _id):
        self.id = _id
        self.users = users
        self.messages = []

    def add_message(self, message):
        self.messages.append(message)

    def add_user(self, user):
        self.users.append(user)

    def get_messages(self):
        return self.messages

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

    def __str__(self):
        return {"name": self.name, "users": self.users, "messages": self.messages}
