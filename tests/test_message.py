import pytest
from message import Message

def test_message_initialization():
    msg = Message("Hello world", "user_alex", "2026-08-01 09:15", "General")
    assert msg.get_content() == "Hello world"
    assert msg.get_author() == "user_alex"
    assert msg.get_timestamp() == "2026-08-01 09:15"
    assert msg.get_category() == "General"
    assert msg.is_flagged() == False

def test_message_flagging():
    msg = Message("Hello world", "user_alex", "2026-08-01 09:15", "General")
    assert msg.is_flagged() == False
    msg.flag()
    assert msg.is_flagged() == True
