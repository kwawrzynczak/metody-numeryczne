from menu import *
from exceptions import *
from nums import *
from numpy import double
from plots import plot

if __name__ == '__main__':

    # MENU UZYTKOWNIKA

    fun = 'str'
    test = [1, 2, 3, 4, 5]
    while fun not in test:
        select_function()
        fun = input('Wybierz funkcje z listy: ')
        fun = check_choice(fun)
        if fun not in test:
            print("Wybierz funkcje z zakresu 1-5!")
        print()

    method = 'str'
    test = [1, 2]
    while method not in test:
        select_method()
        method = input('Wybierz metode: ')
        method = check_choice(method)
        if method not in test:
            print("Wybierz jedna z dwoch metod!")
        print()

    f = globals()[f"function{fun}"]
    left, right = 1, 1
    fl = f(left)
    fr = f(right)
    while fl * fr >= 0:
        try:
            left = double(input('Podaj lewy kraniec przedzialu: '))
            right = double(input('Podaj prawy kraniec przedzialu: '))
            fl = f(left)
            fr = f(right)
        except ValueError:
            print("Wprowadzono nieprawidlowy znak!")
            left, right = 1, 1
        if fl * fr >= 0:
            print("Podane zostaly nieprawidlowe krance przedzialu!")
        print()

    end = 'str'
    test = [1, 2]
    while end not in test:
        select_end()
        end = input('Wybierz warunek zakonczenia programu : ')
        end = check_choice(end)
        if end not in test:
            print("Wybierz jeden z dwoch warunkow!")
        print()

    x, i = double, int
    # ITERACJA -----------------------------------------------

    if end == 1:
        iter = 0
        while iter <= 0:
            iter = input('Podaj ilosc iteracji: ')
            iter = check_choice(iter)
            print()
            if iter <= 0:
                print("Podano nieprawidlowa liczbe iteracji!")
                iter = 0

        if method == 1:
            x, i = bisection_iter(fun, left, right, iter)

        if method == 2:
            x, i = falsi_iter(fun, left, right, iter)

    # EPSILON ------------------------------------------------

    if end == 2:
        eps = -1
        while eps <= 0:
            try:
                eps = double(input('Podaj wartosc epsilona: '))
            except ValueError:
                print("Wprowadzono nieprawidlowy znak")
            if eps <= 0:
                print("Podano nieprawidlowa wartosc epsilona!")
                eps = -1
            print()

        if method == 1:
            x, i = bisection_epsilon(fun, left, right, eps)

        if method == 2:
            x, i = falsi_epsilon(fun, left, right, eps)

    print("x = " + str(x) + "\nRozwiazanie osiagnieto w podana liczbe iteracji: " + str(i))
    # WYKRES FUNKCJI ------------------------------------------

    func = globals()[f"function{fun}"]
    p = 0.001
    start = left
    diff = right - left
    plotx = [0] * int(diff / p)
    ploty = [0] * int(diff / p)
    for i in range(len(plotx)):
        plotx[i] = start
        ploty[i] = func(start)
        start += p

    plot(plotx, ploty)
