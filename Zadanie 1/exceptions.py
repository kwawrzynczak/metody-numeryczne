import sys


def check_choice(select):
    try:
        select = int(select)
        return select
    except ValueError:
        print("Wprowadzono nieprawidlowy znak!")


