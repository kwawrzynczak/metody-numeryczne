from cmath import e

import numpy as np

iterations = 0

def calculate_limit(eps, fun):
    def funkcja_z_waga(x): return fun(x) * e ** (-x ** 2)
    suma = 0
    delta = 0.01

    a = 0
    calka_czastkowa = 2 * eps
    while calka_czastkowa > eps:
        calka_czastkowa = calculate_Simpson(eps, a, a+delta, funkcja_z_waga)
        suma += calka_czastkowa
        a += delta

    a = 0
    calka_czastkowa = 2 * eps
    while calka_czastkowa > eps:
        calka_czastkowa = calculate_Simpson(eps, a-delta, a, funkcja_z_waga)
        suma += calka_czastkowa
        a -= delta

    print(f"ilosc iteracji: {iterations}")
    return suma

def calculate_Simpson(epsilon, a, b, fun):
    result = 0.0
    diff = 10
    iteration = 1
    n = 3

    while diff > epsilon:
        old_result = result
        h = (b - a) / (n - 1)
        x = np.linspace(a, b, n)
        f = fun(x)

        result = (h / 3) * (f[0] + 2 * sum(f[:n - 2:2]) + 4 * sum(f[1:n - 1:2]) + f[n - 1])
        n += 1
        iteration += 1
        diff = abs(result - old_result)

    global iterations
    iterations += iteration
    return result

