import numpy as np


def horner(factors, x):
    result = factors[0]
    for i in range(1, len(factors)):
        result = result * x + factors[i]
    return result


def factorial(n):
    result = 1
    while n > 1:
        result = result * n
        n -= 1
    return result


# np. dla x0;x1 i = 0np.absolute(2 * np.cos(2 * x) + 2)
def diff(x, y, i, j):
    if j - i == 1:
        return (y[j] - y[i]) / (x[j] - x[i])
    else:
        return (diff(x, y, i + 1, j) - diff(x, y, i, j - 1)) / (x[j] - x[i])


def newton_interpolation(nodes_x, function, x):
    n = len(nodes_x)
    y = function(nodes_x)
    W = y[0]
    multiplier = 1

    for i in range(1, n):
        multiplier *= x - nodes_x[i - 1]
        a_i = diff(nodes_x, y, 0, i)
        W += a_i * multiplier

    return W
