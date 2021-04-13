import json
import hashlib

class Termin_3:

    def __init__(self):
        self.data = self.read("T_20210412_data_1.json")
        self.dummy = self.read("T_20210412_data_2.json")
        self.run()

    def run(self):
        self.expand_data()
        self.fuse_related_values()
        self.hash_keys()
        self.write("T_20210412_data_solution.json", self.data)

    def expand_data(self):
        pass

    def fuse_related_values(self):
        pass
     
    def hash_keys(self):
        pass

    def read(self, filename):
        return json.load(open(filename))

    def write(self, filename, data):
        json.dump(data, open(filename, "w"))


Termin_3()
