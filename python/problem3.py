from collections import defaultdict
from itertools import count


def prime_factors(n):
    '''
    Return the prime factorization of n as a defaultdict whose key: value pairs
    indicate the prime: power of prime that factors n.
    '''
    divisor = 2
    odds = count(3, 2)
    results = defaultdict(int)
    while n != 1:
        if n % divisor == 0:
            results[divisor] += 1
            n /= divisor
            continue
        else:
            divisor = next(odds)
    return results


def main():
    '''
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
    '''
    print(max(prime_factors(600851475143)))

if __name__ == '__main__':
    main()
