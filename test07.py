"""
Додайте поле birthday для дня народження в клас Record . Це поле має бути класу Birthday. Це поле не обов'язкове, але може бути тільки одне.
Додайте функціонал роботи з Birthday у клас Record, а саме функцію add_birthday, яка додає день народження до контакту.
Додайте функціонал перевірки на правильність наведених значень для полів Phone, Birthday.
Додайте та адаптуйте до класу AddressBook нашу функцію з четвертого домашнього завдання, тиждень 3, get_upcoming_birthdays, яка для контактів адресної книги повертає список користувачів, яких потрібно привітати по днях на наступному тижні.
Тепер ваш бот повинен працювати саме з функціоналом класу AddressBook - замість словника contacts ми використовуємо book = AddressBook()
"""


class Birthday(Field):
    def __init__(self, value):
        try:
            ...
            # Додайте перевірку коректності даних
            # та перетворіть рядок на об'єкт datetime
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None


"""
Для реалізації нового функціоналу також додайте функції обробники з наступними командами:
add-birthday - додаємо до контакту день народження в форматі DD.MM.YYYY
show-birthday - показуємо день народження контакту
birthdays - повертає список користувачів, яких потрібно привітати по днях на наступному тижні

бот повинен підтримувати наступний список команд:
add [ім'я] [телефон]: Додати або новий контакт з іменем та телефонним номером, або телефонний номер к контакту який вже існує.
change [ім'я] [старий телефон] [новий телефон]: Змінити телефонний номер для вказаного контакту.
phone [ім'я]: Показати телефонні номери для вказаного контакту.
all: Показати всі контакти в адресній книзі.
add-birthday [ім'я] [дата народження]: Додати дату народження для вказаного контакту.
show-birthday [ім'я]: Показати дату народження для вказаного контакту.
birthdays: Показати дні народження, які відбудуться протягом наступного тижня.
hello: Отримати вітання від бота.
close або exit: Закрити програму.


@input_error
def add_birthday(args, book): ...


# реалізація


@input_error
def show_birthday(args, book): ...


# реалізація


@input_error
def birthdays(args, book): ...


# реалізація

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))


        elif command == "change":
            # реалізація

        elif command == "phone":
            # реалізація

        elif command == "all":
            # реалізація

        elif command == "add-birthday":
            # реалізація

        elif command == "show-birthday":
            # реалізація

        elif command == "birthdays":
            # реалізація

        else:
            print("Invalid command.")

"""
