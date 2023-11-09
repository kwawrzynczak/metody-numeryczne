from numpy.polynomial.hermite import hermgauss


def calculate_hermite(fun, n):
    xi, ai = hermgauss(n)
    result = 0.0
    for (a, x) in zip(ai, xi):
        result += fun(x) * a
    return result
