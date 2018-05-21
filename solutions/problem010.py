from problem7 import two_and_odds, is_prime

def main():
    '''
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.
    '''
    result = 0
    for p in two_and_odds():
        if p > 2e6:
            return result

        if is_prime(p):
            result += p


if __name__ == '__main__':
    print(main())
