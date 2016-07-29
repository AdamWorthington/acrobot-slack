
# internal structures:
#   data :: dict
#
# API:
# *all functions return the calling object except get
#   Acronyms() makes a new Acronyms object
#   Acrnyms(filename) returns an Acronyms object from file
#       load(filename) merges Acronyms object from file with current object
#       save(filename) saves current object to file
#       merge(data) merges `data` with current object
#       put(key, val)
#       get(key) returns "" if key could not be found
#
class Acronyms:

    def __init__(self):
        self.data = {}

    def __init__(self, filename):
        self.data = {}
        self.load(filename)

    def merge(self, data):
        self.data = {**self.data, **data}
        return self

    def load(self, filename):
        data = eval(open(filename, 'r').read())
        return self.merge(data)

    def save(self, filename):
        handle = open(filename, 'w')
        handle.truncate()
        handle.write(str(self.data))
        return self

    def put(self, key, val):
        self.data[key] = val
        return self

    def get(self, key):
        if key in self.data:
            return self.data[key]
        else:
            return ""
