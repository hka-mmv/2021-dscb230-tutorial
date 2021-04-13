import json
import hashlib

class Termin_3:

    def __init__(self):
        self.data_1 = self.read("T_20210412_data_1.json")
        self.data_2 = self.read("T_20210412_data_2.json")
        self.run()

    def run(self):
        self.expand_data()
        self.fuse_related_values()
        self.hash_keys()
        self.write("T_20210412_data_solution.json", self.data_1)

    def expand_data(self):
        for dummy_elem in self.data_2:
            for data_elem in self.data_1:
                if data_elem["id"] == dummy_elem["id"]:
                    data_elem["more"] = dummy_elem

    def fuse_related_values(self):
        for elem in self.data_1:
            elem["city"] = (elem["postal_code"], elem["city"])
            elem["country"] = (elem["country"], elem["location"])
            del elem["postal_code"]
            del elem["location"]
     
    def hash_keys(self):
        tmp = {}
        for elem in self.data_1:
            h = hashlib.sha256(elem["more"]["email"].encode("utf-8"))
            tmp[h.hexdigest()] = elem
        self.data_1 = tmp

    def read(self, filename):
        return json.load(open(filename))

    def write(self, filename, data):
        json.dump(data, open(filename, "w"))

Termin_3()
