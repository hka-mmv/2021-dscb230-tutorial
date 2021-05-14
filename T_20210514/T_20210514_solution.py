import numpy as np


def aufgabe_1():
    a = np.array([1, 2, 3])
    print(a)


def aufgabe_2():
    a = np.array([[1, 2], [3, 4]])
    print(a)


def aufgabe_3():
    a = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    print(a)


def aufgabe_4():
    a = np.array([[1, 0, 0],
                  [1, 1, 1],
                  [2, 0, 0]])
    b = np.array([[1, 1, 1],
                  [1, 1, 2],
                  [1, 1, 2]])
    print(a + b)


def aufgabe_5():
    a = np.array([[1, 0, 0],
                  [1, 1, 1],
                  [2, 0, 0]])
    b = np.array([[1, 1, 1],
                  [1, 1, 2],
                  [1, 1, 2]])
    print(a - b)


def aufgabe_6():
    a = np.array([[1, 0, 0],
                  [1, 1, 1],
                  [2, 0, 0]])
    b = np.array([[1, 1, 1],
                  [1, 1, 2],
                  [1, 1, 2]])
    print(a * b)


def aufgabe_7():
    a = np.array([[1, 0, 0],
                  [1, 1, 1],
                  [2, 0, 0]])
    b = np.array([[1, 1, 1],
                  [1, 1, 2],
                  [1, 1, 2]])
    print(a / b)


def aufgabe_8():
    a = np.array([[1, 0, 0],
                  [1, 1, 1],
                  [2, 0, 0]])
    print(np.max(a))
    print(np.min(a))
    print(np.average(a))


def aufgabe_9():
    alice = [99, 101, 103]
    bob = [110, 108, 105]
    trudy = [90, 88, 85]

    salaries = np.array([alice, bob, trudy])
    taxation = np.array([[0.2, 0.25, 0.22],
                         [0.4, 0.5, 0.5],
                         [0.1, 0.2, 0.1]])

    max_income = np.max(salaries - salaries * taxation)
    print(max_income)


def aufgabe_10():
    a = np.array([55, 56, 57, 58, 59, 60, 61])
    print("Ausgang  ", a)
    print("Aufgabe 1", a[:], "keines")
    print("Aufgabe 2", a[2:], "ersten beiden")
    print("Aufgabe 3", a[1:4], "erste und letzten drei")
    print("Aufgabe 4", a[2:-2], "index gerade")
    print("Aufgabe 5", a[::2], "index ungerade")
    print("Aufgabe 6", a[::-1], "invertieren")


def aufgabe_11():
    a = np.array([[0, 1, 2, 3],
                  [4, 5, 6, 7],
                  [8, 9, 10, 11],
                  [12, 13, 14, 15]])

    print("Ausgang  ", a)
    print("Aufgabe 1", a[:, 2], "dritte Spalte")
    print("Aufgabe 2", a[1, :], "zeite Zeile")
    print("Aufgabe 3", a[:, :-1], "alle bis auf die letzte Spalte")


def aufgabe_12():
    a = np.array([1, 2, 3, 4], dtype=np.float64)
    b = np.array([1, 2, 3, 4], dtype=np.int16)
    c = np.array([1, 2, 3, 4], dtype=np.complex)
    print("Aufgabe 1", a, a.dtype)
    print("Aufgabe 2", b, b.dtype)
    print("Aufgabe 3", c, c.dtype)


def aufgabe_13():
    dataScientist = [130, 132, 137]
    productManager = [127, 140, 145]
    designer = [118, 118, 127]
    softwareEngineer = [129, 131, 137]

    employees = np.array([dataScientist,
                          productManager,
                          designer,
                          softwareEngineer])

    employees[0, ::2] = employees[0, ::2] * 1.1
    print(employees)


def aufgabe_14():
    a = np.array([[1, 0, 0],
                  [0, 2, 2],
                  [3, 0, 0]])
    print(a == 2)


def aufgabe_15():
    a = np.array(
        [[42, 40, 41, 43, 44, 43],  # Hong Kong
         [30, 31, 29, 29, 29, 30],  # New York
         [8, 13, 31, 11, 11, 9],  # Berlin
         [11, 11, 12, 13, 11, 12]])  # Montreal
    cities = np.array(["Hong Kong", "New York", "Berlin", "Montreal"])
    polluted = set(cities[np.nonzero(a > np.average(a))[0]])
    print(polluted)


aufgabe_15()
