from collections import UserDict
import re


# Базовий клас для полів запису
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


# Клас для зберігання імені контакту. Обов'язкове поле
class Name(Field):
    pass


# Клас для зберігання номера телефону. Має валідацію формату (10 цифр)
class Phone(Field):
    def __init__(self, phone):
        if not self.validate(phone):
            raise ValueError("Phone number must be 10 digits")
        super().__init__(phone)

    @staticmethod
    def validate(phone):
        return re.match(r"^\d{10}$", phone) is not None


# Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def edit_phone(self, old_phone, new_phone):
        if not self.remove_phone(old_phone):
            print(f"Phone number {old_phone} not found.")
        else:
            self.add_phone(new_phone)

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p.value
        return None

    def remove_phone(self, phone):
        if self.find_phone(phone) is None:
            print(f"Phone number {phone} not found. Cannot remove.")
            return False
        else:
            self.phones = [p for p in self.phones if p.value != phone]
            print(f"Removed phone number: {phone}")
            return True

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


# Клас для зберігання та управління записами
class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())


"""Checkup block:"""

# Створення нової адресної книги
book = AddressBook()

# Додавання записів
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
print("All contacts in the address book:")
print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")
print("After editing John's phone:")
print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name.value}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")
print("After deleting Jane:")
print(book)
