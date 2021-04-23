import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

class Termin5:

    def __init__(self, filename, x_label, y_label, title):
        # Read the CSV Data with Pandas
        self.data = pd.read_csv(filename)
        # Read the Keys out of the Data
        self.x = pd.DataFrame(self.data[x_label])
        self.y = pd.DataFrame(self.data[y_label])
        # Set the L.R. Model
        self.model = LinearRegression().fit(self.x, self.y)

        self.draw(x_label, y_label, title)

    def draw(self, x_label, y_label, title, alpha=0.7):
        # Calc the Linear Regression
        lr = np.array([min(self.x.loc[:, x_label]), max(        # loc = Access a group of rows and
            self.x.loc[:, x_label])]).reshape(-1, 1)            # columns by label(s) or a boolean array

        # Draw the Data into the Plot
        plt.scatter(self.data[x_label], self.data[y_label], marker="x")
        plt.plot(lr, self.model.predict(lr), "-r")

        # Set additional content (Labels, ...)
        plt.gcf().canvas.set_window_title("DSCB 230")
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)

        plt.show()


Termin5("T_20210423_fish.csv", "Laenge", "Gewicht",
        "Fisch Größe und Gewicht in Relation")
Termin5("T_20210423_gold.csv", "Jahr", "Preis",
        "Entwicklung des Goldpreises über die Jahre")
Termin5("T_20210423_heart.csv", "Alter", "Puls",
        "Alter und Puls bei Herzinfakrten in Relation")


