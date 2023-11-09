from matplotlib import pyplot as plt


def plot(x, y):
    plt.plot(x, y, 'red')
    plt.axis('square')
    plt.axhline(y=0, color='black')
    plt.axvline(color='black')
    plt.show()

