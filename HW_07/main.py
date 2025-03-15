# main.py
#!/usr/bin/python
# -*- coding: utf-8 -*-

from assist_bot import (
    add_contact,
    change_contact,
    delete_contact,
    show_phone,
    show_all,
    add_birthday,
    show_birthday,
    birthdays,
    parse_input,
)
from address_book import AddressBook


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        name_input = input("Enter a command: ")
        command, args = parse_input(name_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "all":
            print(show_all(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(args, book))
        elif command == "change":
            if len(args) < 2:
                print("Please provide: name & new value")
            elif len(args) == 3:
                name, old_phone, new_phone = args
                result = change_contact(name, old_phone, new_phone, book)
                print(result)
            else:
                print("Change command not recognized. Please specify what to change.")
        elif command == "delete":
            if len(args) != 1:
                print("Please provide the name of the contact to delete.")
            else:
                name = args[0]
                result = delete_contact(name, book)
                print(result)
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
