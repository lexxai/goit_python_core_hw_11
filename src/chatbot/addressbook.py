from collections import UserDict
from datetime import date

class AddressBook(UserDict):

    def add_record(self, rec):
        key = rec.name.value
        self.data[key] = rec
    
    def get_record(self, key):
        return self.data[key]

    def remove_record(self, key):
        del self.data[key]

    def __repr__(self):
        return str(self)

    def get_csv(self):
        result = [Record.get_csv_header()]
        result.extend([ str(r.get_csv_row()) for r in self.data.values() ])
        return "\n".join(result)
    
    def __str__(self):
        result = map(str, self.data.values())
        return "\n".join(result)

class Field:

    def __init__(self, value: str) -> None:
        self.value = value

    def __eq__(self, other):
        return self.value == other

    def __repr__(self):
        return str(self)

    def __str__(self) -> str:
        return str(self.value)


class Name(Field):
    ...


class Address(Field):
    ...


class Email(Field):

    def __init__(self, value: str) -> None:
        if not (value and '@' in value):
            value = None
        super().__init__(value)


class Phone(Field):
    def __init__(self, value: str) -> None:
        value = str(int(value))
        super().__init__(value)


class Birthday(Field):
    def __init__(self, value: str) -> None:
        self.value_date = date.fromisoformat(value)
        super().__init__(value)

class Record:

    def __init__(self, name: Name, phone: Phone = None,
                 email: Email = None, address: Address = None) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.phones = []
        self.add_phone(phone)
        self.birthday = None

    def add(self, field: Field) -> bool:
        if isinstance(field, Phone):
            return self.add_phone(field)
            
    def remove(self, field: Field) -> bool:
        if isinstance(field, Phone):
            return self.remove_phone(field)
   
    def add_phone(self, phone: Phone) -> None:
        if (phone):
            if (isinstance(phone, list)):
                for ph in phone:
                    if ph not in self.phones:
                        self.phones.append(ph)
            elif phone not in self.phones:
                self.phones.append(phone)
            return True
            
    def change_phone(self, old_phone: Phone, new_phone: Phone) -> None:
        if old_phone and new_phone:
            self.remove_phone(old_phone)
            self.add_phone(new_phone)

    def remove_phone(self, phone: Phone) -> None:
        self.phones.remove(phone)
        return True

    def get_phones(self) -> str:
        return ";".join([ str(ph) for ph in self.phones])

    def get_csv_row(self) -> str:
        cols = [str(self.name),self.get_phones(),str(self.email),str(self.address)]
        return ",".join(cols)
    
    @staticmethod
    def get_csv_header() -> str:
        cols = ["name","phone","email","address"]
        return ",".join(cols)

    def add_birthday(self, birthday: Birthday) -> None:
        self.birthday = birthday
    
    def delete_birthday(self) -> None:
        self.birthday = None

    def days_to_birthday(self) -> int:
        result = None
        if self.birthday:
            date_now = date.today()
            date_now_year = date_now.year
            bd = self.birthday.value_date.replace(year=date_now_year)
            if bd < date_now:
                date_now_year += 1
            bd = self.birthday.value_date.replace(year=date_now_year)
            diff_bd = bd - date_now
            result = diff_bd.days

        return result



    def __repr__(self):
        return str(self)

    def __str__(self) -> str:
        cols = [f"name: {self.name}"]
        phone = self.phones
        if len(phone):
            cols.append(f"phones: {self.get_phones()}")
        if self.email:
            cols.append(f"email: {self.email}")
        if self.address:
            cols.append(f"address: {self.address}")    
        return ", ".join(cols)

