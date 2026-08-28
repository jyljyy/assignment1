import csv
from src.message import Message
from src.spam_message import SpamMessage
from src.shouting_message import ShoutingMessage
class Moderator:
    def __init__(self):
        self.messages = []

    def add_message(self, message):

    def list_messages(self):
        if not self.messages:
            print("No messages in the system.")
            return
        for i, msg in enumerate(self.messages, start=1):
            print(f"{i}. {msg}")

    def flag_message(self, index):
        if index < 1 or index > len(self.messages):
            print("Invalid message number.")
            return
        message = self.messages[index - 1]
        message.flag()
        print("Message flagged successfully.")

    def display_message_details(self, index):
        if index < 1 or index > len(self.messages):
            print("Invalid message number.")
            return
        message = self.messages[index - 1]
        print(f"Content: {message.get_content()}")
        print(f"Author: {message.get_author()}")
        print(f"Category: {message.get_category()}")
        print(f"Timestamp: {message.get_timestamp()}")
        print(f"Flagged: {'Yes' if message.is_flagged() else 'No'}")

    def search_by_category(self, category):
        results = []
        for msg in self.messages:
            if msg.get_category().lower() == category.lower():
                results.append(msg)
        return results

    def search_by_author(self, author):
        results = []
        for msg in self.messages:
            if msg.get_author().lower() == author.lower():
                results.append(msg)
        return results

    def search_by_flagged_status(self, flagged):
        results = []
        for msg in self.messages:
            if msg.is_flagged() == flagged:
                results.append(msg)
        return results
