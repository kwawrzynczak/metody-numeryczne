from horner import horner
import numpy as np


def function1(x):  # y = x^3-x^2-2x+1
    tab = [1, -1, -2, 1]
    return horner(tab, len(tab), x)


def function2(x):
    return np.sin(x) - np.cos(x)


def function3(x):  # y = 2^x-3x
    return 2 ** x - 3 * x


def function4(x):  # y = tg(x) - 1
    return np.sin(x)/np.cos(x) - 1


def function5(x):
    return np.cos(x) + x ** 3 - 1