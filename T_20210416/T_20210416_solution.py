import json
import matplotlib.pyplot as plt

class Termin_4:

    def __init__(self):
        self.data = self.read("T_20210416.json")
        self.run()

    def run(self):
        self.draw(self.count_key("sector"))

    def count_key(self, key):
        counter = {}
        for elem in self.data:
            value = elem[key]
            counter[value] = counter[value] + 1 if value in counter else 1
        return counter 

    def draw(self, data): 
        fig, axs = plt.subplots(2)
        fig.canvas.set_window_title("DSCB 230") 
        fig.suptitle("Börsen Sektoren Vergleich")
        
        axs[0].plot(*zip(*data.items()))
        axs[1].bar(*zip(*data.items()))
        
        for ax in axs.flat:
            ax.label_outer()
    
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()

    def read(self, filename):
        return json.load(open(filename))

    def write(self, filename, data):
        json.dump(data, open(filename, "w"))

Termin_4()
