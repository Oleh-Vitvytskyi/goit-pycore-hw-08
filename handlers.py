from models import AddressBook, Record
from utils import input_error
import pickle

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            try:
                return pickle.load(f)
            except EOFError:
                return AddressBook()  
    except FileNotFoundError:
        return AddressBook()
    
@input_error
def add_contact(args, book: AddressBook):
    if len(args) < 2:
        raise ValueError("You must provide a name and phone number.")
    name, phone = args[0], args[1]
    record = book.find(name)
    if not record:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    else:
        message = "Contact updated."
    record.add_phone(phone)
    return message

@input_error
def change_contact(args, book: AddressBook):
    if len(args) < 3:
        raise ValueError("You must provide a name, old phone, and new phone number.")
    name, old_phone, new_phone = args
    record = book.find(name)
    if not record:
        raise KeyError("Contact not found.")
    for phone in record.phones:
        if phone.value == old_phone:
            phone.value = new_phone
            return "Phone number updated."
    return "Old phone number not found."

@input_error
def get_phone(args, book: AddressBook):
    if len(args) < 1:
        raise IndexError("You must provide a name.")
    name = args[0]
    record = book.find(name)
    if not record:
        raise KeyError("Contact not found.")
    phones = [phone.value for phone in record.phones]
    return f"Phone numbers for {name}: {', '.join(phones)}"

@input_error
def list_all_contacts(book: AddressBook):
    if not book.records:
        return "No contacts found."
    result = []
    for record in book.records.values():
        phones = ", ".join([phone.value for phone in record.phones])
        result.append(f"{record.name.value}: {phones}")
    return "\n".join(result)

@input_error
def add_birthday(args, book: AddressBook):
    if len(args) < 2:
        raise ValueError("You must provide a name and a birthday in DD.MM.YYYY format.")
    name, birthday = args[0], args[1]
    record = book.find(name)
    if not record:
        return "Contact not found."
    record.add_birthday(birthday)
    return "Birthday added."

@input_error
def show_birthday(args, book: AddressBook):
    if len(args) < 1:
        raise ValueError("You must provide a name.")
    name = args[0]
    record = book.find(name)
    if not record:
        return "Contact not found."
    return record.get_birthday()

@input_error
def birthdays(args, book: AddressBook):
    upcoming_birthdays = book.get_upcoming_birthdays()
    if not upcoming_birthdays:
        return "No upcoming birthdays."
    return "\n".join([f"{b['name']}: {b['birthday']}" for b in upcoming_birthdays])