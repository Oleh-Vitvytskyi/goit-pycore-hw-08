from datetime import datetime, timedelta

class Field:
    def __init__(self, value):
        self.value = value

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must contain exactly 10 digits.")
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
    
    def add_phone(self, phone):
        self.phones.append(Phone(phone))
    
    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)
    
    def get_birthday(self):
        if self.birthday:
            return self.birthday.value.strftime("%d.%m.%Y")
        return "No birthday set"

class AddressBook:
    def __init__(self):
        self.records = {}
    
    def add_record(self, record):
        self.records[record.name.value] = record
    
    def find(self, name):
        return self.records.get(name)
    
    def get_upcoming_birthdays(self):
        upcoming_birthdays = []
        today = datetime.now()
        end_date = today + timedelta(days=7)
        for record in self.records.values():
            if record.birthday:
                birthday_this_year = record.birthday.value.replace(year=today.year)
                if today <= birthday_this_year <= end_date:
                    upcoming_birthdays.append({
                        "name": record.name.value,
                        "birthday": birthday_this_year.strftime("%d.%m.%Y")
                    })
        return upcoming_birthdays
