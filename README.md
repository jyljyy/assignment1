# Content Moderation System

## Project Description
A functional command-line interface using Object-Orientated Progtamming (OOP) principles in Python that allows users to interact with the system. This user interface allows the Willow. Community moderator to scan and filter the messages coming through and flag anything that needs human review instead of having the staff manually scan every single messages for red flags. The system also doesnt automaticallly delete any posts, instead filters it to 2 different categories, 'ok to ignore' and 'someone should take a look at it'. The moderator is also able to perform other functions such as add new message, search and save to csv file.

## Installation
Step 1: Clone the repository
'''bash
git clone <https://github.com/jyljyy/assignment1.git>
cd assignment1 
'''

Step 2: Ensure you have Python 3.7 or later 
'''bash
python3 --version #or the equilavent for your own device
'''

Step 3: Install the required dependencies
'''bash
pip3 install -r requirements.txt #or the equilavent for your own device
'''

## Usage
Run the program from the project root:
```bash
python3 src/main.py
```

You'll see a menu:
=== Content Moderation System ===
1. List all messages
2. Add a new message
3. Search for a message
4. Flag a message
5. Display message details
6. Save moderator data
7. Load moderator data
8. Exit
Enter your choice (1-8): 

What each number means:
1. List all messages — shows every message currently in the system, including its category and whether it's been flagged.

2. Add a new message — prompts for message content, author, and category (spam/shouting), then adds it to the system.

3. Search for a message — search by category, author, or flagged status, and view matching results.

4. Flag a message — mark a specific message as flagged for moderator review.

5. Display message details — view full details (content, author, category, timestamp, flagged status) for one specific message.

6. Save moderator data — writes all current messages to `data/messages.csv`.

7. Load moderator data — loads messages from `data/messages.csv` into the system. Run this first to see the sample data included with this project.

8. Exit — closes the program.


## Testing
Unit tests for the Message class can be found under test/test_messages.py. To run testing, go to terminal:
'''bash
pytest
'''

The expcted output:
============== test session starts ==============
platform darwin -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0
rootdir: #file name and saved location
configfile: pytest.ini
collected 2 items                               

tests/test_message.py ..                  [100%]

=============== 2 passed in 0.01s ===============