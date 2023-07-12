from collections import UserDict
from chatbot.record import Record

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







