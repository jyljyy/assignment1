import csv
from message import Message
from spam_message import SpamMessage
from shouting_message import ShoutingMessage
class Moderator:
    def __init__(self):
        self.messages = []

    def add_message(self, message):
        self.messages.append(message)

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

    def save_data(self, filepath):
        with open(filepath, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Content', 'Author', 'Timestamp', 'Category', 'Flagged'])
            for i, msg in enumerate(self.messages, start=1):
                writer.writerow([
                    i,
                    msg.get_content(),
                    msg.get_author(),
                    msg.get_timestamp(),
                    msg.get_category(),
                    msg.is_flagged()
                ])
        print(f"Data saved to {filepath}")

    def load_data(self, filepath):
        self.messages = []
        with open(filepath, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                category = row['Category']
                flagged = row['Flagged'] == 'True'

                if category == 'Spam':
                    msg = SpamMessage(row['Content'], row['Author'], row['Timestamp'])
                elif category == 'Shouting':
                    msg = ShoutingMessage(row['Content'], row['Author'], row['Timestamp'])
                else:
                    msg = Message(row['Content'], row['Author'], row['Timestamp'], category)

                if flagged:
                    msg.flag()

                self.messages.append(msg)
        print(f"Data loaded from {filepath}")