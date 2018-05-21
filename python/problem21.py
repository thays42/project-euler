from math import sqrt

def divisors(n, proper=False):
    proper_divisors = {x for x in range(1, int(sqrt(n)) + 1) if n % x == 0}

    if proper:
        return proper_divisors
    else:
        return proper_divisors.union([n])

def main():
    '''
    Let d(n) be defined as the sum of proper divisors of n (numbers less than n
    which divide evenly into n). If d(a) = b and d(b) = a, where a != b, then a
    and b are an amicable pair and each of a and b are called amicable numbers.

    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44,
    55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4,
    71 and 142; so d(284) = 220.

    Evaluate the sum of all the amicable numbers under 10000.
    '''

    history, answer = dict(), 0
    for n in range(1, 10000):
        dn = sum(divisors(n, proper=True))
        if history.get(dn, 0) == n and n != dn:
            answer += n + dn
        else:
            history[n] = dn
    return answer

if __name__ == '__main__':
    print(main())
