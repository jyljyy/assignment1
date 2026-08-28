from message import Message

class ShoutingMessage(Message):
    def __init__(self, content, author, timestamp):
        super().__init__(content, author, timestamp, category="Shouting")

    def get_category(self):
        return "Shouting"
