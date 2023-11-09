import numpy as np
from exceptions import check_choice
import pylab as pb
from maths import newton_interpolation
from read_file import read_file
from functions import *

if __name__ == '__main__':
    # MENU UZYTKOWNIKA

    formula1 = 'f(x) = x^3 - x^2 - 2x + 1'
    formula2 = 'f(x) = sin(x) - cos(x)'
    formula3 = 'f(x) = x - 10'
    formula4 = 'f(x) = |x|'
    formula5 = 'f(x) = |2 * cos(2x) + 2|'

    fun = 'str'
    test = [1, 2, 3, 4, 5]
    while fun not in test:
        print('1. ' + str(formula1))
        print('2. ' + str(formula2))
        print('3. ' + str(formula3))
        print('4. ' + str(formula4))
        print('5. ' + str(formula5))

        fun = input('Wybierz funkcje z listy: ')
        fun = check_choice(fun)

        if fun not in test:
            print("Wybierz funkcje z zakresu 1-5!")
        print()

    left, right = 1, 0
    while left >= right:
        try:
            left = np.double(input('Podaj lewy kraniec przedzialu: '))
            right = np.double(input('Podaj prawy kraniec przedzialu: '))
            if left >= right:
                print("Podane zostaly nieprawidlowe krance przedzialu!")
        except ValueError:
            print("Wprowadzono nieprawidlowy znak!")
        print()

    func = globals()[f"function{fun}"]
    form = globals()[f"formula{fun}"]

    nodes_x, nodes = read_file()

    nodes_x = np.double(nodes_x)
    nodes_y = func(nodes_x)

    calculated_x, calculated_y = [], []
    left = np.double(left)
    right = np.double(right)

    h = 0.01

    arguments, values = [], []

    while left <= right:
        calculated_x.append(left)
        calculated_y.append(newton_interpolation(nodes_x, func, left))
        arguments.append(left)
        values.append(func(left))
        left += h

    average_err = (sum(values) - sum(calculated_y)) / len(calculated_y)
    print(f"Blad przyblizonej wartosci funkcji f(x): {average_err}")

    pb.plot(arguments, values, label='Wykres funkcji f(x)', color='red')
    pb.title(form)

    pb.scatter(nodes_x, nodes_y)
    pb.plot(calculated_x, calculated_y, linestyle='dashed', color='green')
    pb.grid(True)

    pb.axhline(y=0, color='k')
    pb.axvline(x=0, color='k')

    pb.show(block=True)

    a = 1
    while a:
        x1 = np.double(input('Podaj argument, którego wartość chcesz odczytać: '))
        y1 = newton_interpolation(nodes_x, func, x1)
        y2 = func(x1)
        blad = y2 - y1

        print(f'Obliczona wartosc funkcji f({x1}) = {y1}')
        print((f'Rzeczywista wartosc funkcji f({x1}) = {y2}'))
        print(f'Blad przyblizonej wartosci funkcji w punkcie {x1}: {blad}')


        pb.plot(arguments, values, label='Wykres funkcji f(x)', color='red')
        pb.title(form)

        pb.scatter(x1, y1)
        pb.plot(calculated_x, calculated_y, linestyle='dashed', color='green')
        pb.grid(True)

        pb.axhline(y=0, color='k')
        pb.axvline(x=0, color='k')

        pb.show(block=True)
        a = int(input('Czy chcesz wpisac kolejną wartość? 0/1'))
