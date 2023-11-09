import sys
import numpy as np


def read_file(filename):
    try:
        matrix = np.loadtxt(f'eq/{filename}.txt')
        A = matrix
        return A

    except ValueError:
        sys.exit("Macierz jest nieprawidłowa!")


def get_filename():
    try:
        choice = input("Wprowadź nazwę pliku bez rozszerzenia: ")
        return read_file(choice)

    except FileNotFoundError:
        print("Podany plik nie istnieje!\n")
        return None
