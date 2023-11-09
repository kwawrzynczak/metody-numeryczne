from maths import horner
import numpy as np


def function1(x):  # y = x^3-x^2-2x+1 WIELOMIAN
    tab = [1, -1, -2, 1]
    return horner(tab, x)


def function2(x):  # TRYGONOMETRYCZNA
    return np.sin(x) - np.cos(x)


def function3(x):  # y = x - 10 LINIOWA
    return x - 10


def function4(x):  # y = |x| WARTOŚĆ BEZWZGLĘDNA
    return abs(x)


def function5(x):  # y = |2 * cos(2x) + 2| ZŁOŻENIE
    return np.absolute(2 * np.cos(2 * x) + 2)
