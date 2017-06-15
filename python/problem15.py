from math import factorial

def choose(n, k):
    return int(factorial(n) / factorial(k) / factorial(n-k))

def main():
    '''
    Starting in the top left corner of a 2×2 grid, and only being able to move
    to the right and down, there are exactly 6 routes to the bottom right
    corner.

    How many such routes are there through a 20×20 grid?
    '''

    return choose(40, 20)


if __name__ == '__main__':
    print(main())
