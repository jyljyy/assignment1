from message import Message

class SpamMessage(Message):
    def __init__(self, content, author, timestamp):
        super().__init__(content, author, timestamp, category="Spam")

    def get_category(self):
        return "Spam"