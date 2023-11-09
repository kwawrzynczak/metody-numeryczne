from read_file import get_filename
from gauss_elimination import row_operations, back_substitution
import numpy as np

if __name__ == '__main__':
    # WPROWADZENIE WSPOLCZYNNIKOW Z PLIKU

    A = None
    while A is None:
        A = get_filename()

    n = len(A)
    x = np.zeros(n)
    #  ----------------------------------

    print(A)

    row_operations(A)

    print(A)

    back_substitution(A, x)
