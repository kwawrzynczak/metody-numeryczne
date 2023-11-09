import sys

import numpy as np
from numpy import double
from Hermite import calculate_hermite
from Newton_Cotes import calculate_limit


def check_choice(select):
    try:
        select = int(select)
        return select
    except ValueError:
        print("\nWprowadzono nieprawidlowy znak!")


if __name__ == '__main__':
    while True:
        # WYBOR FUNKCJI
        choice = 'str'
        test = {0, 1, 2, 3, 4}
        while choice not in test:
            print('0. WYJŚCIE Z PROGRAMU')
            print('1. x^2 + 3')
            print('2. cos(2x)')
            print('3. 4log(x+3)')
            print('4. |x - 2|')

            choice = input('\nWybierz funkcję z listy: ')
            choice = check_choice(choice)

            if choice not in test:
                print("\nWybierz funkcję z zakresu 1-4!")
            print()

        # PRZYPISANIE FUNKCJI
        def fun(x): return x
        if choice == 0:
            sys.exit()
        if choice == 1:
            def fun(x): return x * x + 3
        if choice == 2:
            def fun(x): return np.cos(2 * x)
        if choice == 3:
            def fun(x): return np.log(x + 3) * 4
        if choice == 4:
            def fun(x): return abs(x-2)

        # DOKLADNOSC OBLICZEN
        eps = -1
        while eps <= 0:
            try:
                eps = double(input('Podaj dokładność: '))
            except ValueError:
                print("Wprowadzono nieprawidlowy znak")
            if eps <= 0:
                print("Podano nieprawidlowa wartosc epsilona!")
                eps = -1
            print()

        # METODA NEWTONA-COTESA, WZOR SIMPSONA
        print("Metoda Newtona-Cotesa oparta na trzech węzłach: ")
        result = calculate_limit(eps, fun)
        print(f'Całka wynosi: {result}')

        # METODA GAUSSA-HERMITE'A
        print("\nKwadratura Gaussa-Hermite'a: ")
        print(f"2 węzły: {calculate_hermite(fun, 2)}")
        print(f"3 węzły: {calculate_hermite(fun, 3)}")
        print(f"4 węzły: {calculate_hermite(fun, 4)}")
        print(f"5 węzły: {calculate_hermite(fun, 5)}")
        print()
