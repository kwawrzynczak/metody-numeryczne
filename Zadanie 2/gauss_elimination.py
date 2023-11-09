import numpy as np
import sys


def row_operations(A):  # wszystkie współczynniki pod przekątną = 0 (macierz górnotrójkątna)
    for i in range(len(A)):
        if (i + 1) < len(A):
            if A[i][i] < A[i + 1][i]:
                for j in range(len(A) + 1):
                    temp = A[i][j]
                    A[i][j] = A[i + 1][j]
                    A[i + 1][j] = temp

    for i in range(len(A)):

        if A[i][i] == 0.0:
            return -1

        for j in range(i + 1, len(A)):
            ratio = A[j][i] / A[i][i]
            for k in range(len(A) + 1):
                A[j][k] = A[j][k] - ratio * A[i][k]

    return A


def back_substitution(A, x):
    n = len(A)
    is_all_zero = False
    is_zero = False
    a = np.delete(A, (len(A)), axis=1)

    for i in range(n):
        if np.all(abs(a[i]) < 0.0001):
            is_zero = True
        if np.all(abs(A[i]) < 0.0001):
            is_all_zero = True
            is_zero = False

    if is_all_zero:
        print("\nPodany układ jest układem nieoznaczonym! ")
        exit()

    if is_zero:
        print("\nPodany układ jest układem sprzecznym! ")
        exit()

    else:
        # w ostatnim wierszu, x_n = wyrazowi wolnemu podzielonemu przez ostatni współczynnik
        x[n - 1] = A[n - 1][n] / A[n - 1][n - 1]

        # przechodzimy do wcześniejszego wiersza
        # x_i = wyraz wolny - ostatni obliczony x_ * przedostatni element w wierszu
        for i in range(n - 2, -1, -1):
            x[i] = A[i][n]
            for j in range(i + 1, n):
                x[i] = x[i] - A[i][j] * x[j]

            # dzielimy przez A[i][i]
            x[i] = x[i] / A[i][i]

        print("\nRozwiązania układu: ", x)
