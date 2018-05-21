from problem3 import prime_factors
from functools import reduce
from collections import defaultdict
import operator


def product(collection):
    return reduce(operator.mul, collection, 1)


def main():
    '''
    2520 is the smallest number that can be divided by each of the numbers from 1 to
    10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the
    numbers from 1 to 20?
    '''

    # Figure out the max power of each prime factor in 2..20
    factors = defaultdict(int)
    for pf in [prime_factors(i) for i in range(2, 21)]:
        for k, v in pf.items():
            factors[k] = max(factors[k], v)

    return product(k**v for k, v in factors.items())

if __name__ == '__main__':
    print(main())
