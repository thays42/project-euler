from math import sqrt
from itertools import count

def two_and_odds():
    '''
    Helper generator for search space of prime numbers
    '''
    result = 2
    odds = count(3, 2)
    while True:
        yield result
        result = next(odds)


def is_prime(n):
    '''
    Logical; Limits search space to 2, 3, 5, ..., sqrt(n)
    '''
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        return all(n % x != 0 for x in range(3, int(sqrt(n))+1, 2))


def main():
    '''
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
    that the 6th prime is 13.

    What is the 10 001st prime number?
    '''
    for i, p in enumerate(x for x in two_and_odds() if is_prime(x)):
        if i == 10_000:
            return p

if __name__ == '__main__':
    print(main())
