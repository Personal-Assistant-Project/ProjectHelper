from contacts_list import *


def main():
    while True:
        user_input = input("Hello, I'm your personal helper. What can I do for you today?:\n1. Load contact's list\n2. Create new contact's list\n\
3. Work with notes\n4. Sort your folders")
        if user_input == 'exit':
            print('Bye!')
            break


if __name__ == '__main__':
    main()