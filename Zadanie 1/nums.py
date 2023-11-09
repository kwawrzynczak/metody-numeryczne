from functions import *
from nums import *
from horner import *


def bisection_epsilon(fun_nr, left, right, eps):
    fun = globals()[f"function{fun_nr}"]
    i = 0
    x = (left + right) / 2
    while (abs(fun(x))) > eps and fun(x) != 0:
        x = (left + right) / 2
        if fun(left) * fun(x) < 0:
            right = x
        else:
            left = x
        i += 1

    return x, i


def bisection_iter(fun_nr, left, right, iter):
    fun = globals()[f"function{fun_nr}"]
    i = 0
    x = (left + right) / 2
    while i < iter and fun(x) != 0:
        x = (left + right) / 2
        if fun(left) * fun(x) < 0:
            right = x
        else:
            left = x
        i += 1

    return x, i


def falsi_epsilon(fun_nr, left, right, eps):
    fun = globals()[f"function{fun_nr}"]
    i = 0
    c = True
    x = left - (right - left) * fun(left) / (fun(right) - fun(left))
    while c and fun(x) != 0:
        x = left - (right-left) * fun(left)/(fun(right) - fun(left))

        if fun(left)*fun(x) < 0:
            right = x
        else:
            left = x
        i += 1
        c = abs(fun(x)) > eps

    return x, i


def falsi_iter(fun_nr, left, right, iter):
    fun = globals()[f"function{fun_nr}"]
    i = 0
    x = left - (right - left) * fun(left) / (fun(right) - fun(left))
    while i < iter and fun(x) != 0:
        if fun(right) - fun(left) == 0:
            return x, i
        x = left - (right - left) * fun(left) / (fun(right) - fun(left))

        if fun(left) * fun(x) < 0:
            right = x
        else:
            left = x
        i += 1

    return x, i
