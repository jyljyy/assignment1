from moderator import Moderator
from spam_message import SpamMessage
from shouting_message import ShoutingMessage
from datetime import datetime

def main():
    moderator = Moderator()
    
    while True:
        print("\n=== Content Moderation System ===")
        print("1. List all messages")
        print("2. Add a new message")
        print("3. Search for a message")
        print("4. Flag a message")
        print("5. Display message details")
        print("6. Save moderator data")
        print("7. Load moderator data")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ")
        
        if choice == '1':
            moderator.list_messages()

        elif choice == '2':
            content = input("Enter message content: ")
            author = input("Enter author's username: ")
            category = input("Enter category (spam/shouting): ")
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            
            if category.lower() == "spam":
                new_message = SpamMessage(content, author, timestamp)
            elif category.lower() == "shouting":
                new_message = ShoutingMessage(content, author, timestamp)
            else:
                print("Invalid category. Message not added.")
                continue

            moderator.add_message(new_message)
            print("Message added successfully.")

        elif choice == '3':
            print("1. By category (spam/shouting)")
            print("2. By author")
            print("3. By flagged status")
            search_choice = input("Enter your choice (1-3): ")
            
            if search_choice == '1':
                category = input("Enter category (spam/shouting): ")
                results = moderator.search_by_category(category)
            elif search_choice == '2':
                    author = input("Enter author: ")
                    results = moderator.search_by_author(author)
            elif search_choice == '3':
                    flagged_input = input("Search flagged messages? (yes/no): ")
                    flagged = flagged_input.lower() == 'yes'
                    results = moderator.search_by_flagged_status(flagged)
            else:
                print("Invalid choice.")
                continue
            
            if not results:
                print("No matching messages found.")
            else:
                print("Search Results:")
                for msg in results:
                    print(msg)

        elif choice == '4':
            index = int(input("Enter the message number to flag: "))
            moderator.flag_message(index)
        elif choice == '5':
            index = int(input("Enter the message ID: "))
            moderator.display_message_details(index)

        elif choice == '6':
            moderator.save_data("data/messages.csv")

        elif choice == '7':
            moderator.load_data("data/messages.csv")

        elif choice == '8':
            print("Thank you for using the Content Moderation System!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
