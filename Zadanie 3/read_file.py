import sys


def read_file():
    with open("data.txt", 'r') as data:
        nodes_x = data.readline().split()
    data.close()
    nodes = len(nodes_x)
    if nodes > 1:
        return nodes_x, nodes
    else:
        sys.exit('Liczba wezlow w pliku musi być większa niz jeden!')
