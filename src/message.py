class Message:
    def __init__(self, content, author, timestamp, category):
        """initialise with content, author, timestamp and category. 
        Messages are not flagged by default"""
        self._content = content
        self._author = author
        self._timestamp = timestamp
        self._category = category
        self._flagged = False  

    def get_content(self):
        return self._content

    def get_author(self):
        return self._author

    def get_timestamp(self):
        return self._timestamp

    def get_category(self):
        return self._category

    def is_flagged(self):
        return self._flagged

    def flag(self):
        self._flagged = True

    def __str__(self):
        """returns a string representation of the message, including its content, category, author, and flagged status"""
        flag_marker = " [FLAGGED]" if self._flagged else ""
        return f'"{self._content}" ({self.get_category()}, from {self._author}){flag_marker}'