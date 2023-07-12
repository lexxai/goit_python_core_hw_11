from datetime import date

# Parent class
class Field:

    def __init__(self, value: any) -> None:
        self.value = value

    def __eq__(self, __other):
        if isinstance(__other, Field):
            return self.value == __other.value
        else:
            raise TypeError

    def __repr__(self):
        return str(self)

    def __str__(self) -> str:
        return str(self.value)

# Child classes 
class Name(Field):
    ...


class Address(Field):
    ...


class Email(Field):

    def __init__(self, value: str) -> None:
        self.__value = None
        self.value = value
        super().__init__(value)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, __new_value):
        if not (__new_value and '@' in __new_value):
            __new_value = None
        self.__value = __new_value


class Phone(Field):

    def __init__(self, value: str) -> None:
        self.__value = None
        self.value = value
        super().__init__(value)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, __new_value):
        self.__value = str(int(__new_value))


class Birthday(Field):

    def __init__(self, value: str) -> None:
        self.__value = None
        self.value = value
        super().__init__(value)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, __new_value):
        self.__value = date.fromisoformat(__new_value)

    def __str__(self):
        return self.value.isoformat()
