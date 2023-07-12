from collections import UserDict
from chatbot.record import Record

class AddressBook(UserDict):

    def __init__(self, records_per_page=10, *args, **kwargs):
        self.max_records_per_page = records_per_page
        super().__init__(self, *args, **kwargs)

    def add_record(self, rec):
        key = rec.name.value
        self.data[key] = rec
    
    def get_record(self, key):
        return self.data[key]

    def remove_record(self, key):
        del self.data[key]

    def len(self):
        return len(self.data)

    def __repr__(self):
        return str(self)

    def get_csv(self):
        result = [Record.get_csv_header()]
        result.extend([ str(r.get_csv_row()) for r in self.data.values() ])
        return "\n".join(result)
    
    def __str__(self):
        #result = map(str, self.data.values())
        result = [ str(i) for i in self.data.values() ]
        return "\n".join(result)

    def __iter__(self):
        self._page_pos = 0
        return self

    def __next__(self):
        #print("start __next__", self._page_pos)
        if self._page_pos < len(self.data.keys()):
            result = []
            keys = list(self.data)[self._page_pos:self._page_pos+self.max_records_per_page]
            #print("__next__", self._page_pos, keys)
            for key in keys:
                result.append(self.data[key])
            self._page_pos += self.max_records_per_page
            return result
        self._page_pos = 0
        #print("StopIteration", self._page_pos)
        raise StopIteration





