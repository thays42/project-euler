from math import sqrt

def fibonacci(n):
    '''
    Closed form function for the nth fibonacci number
    https://en.wikipedia.org/wiki/Fibonacci_number#Closed-form_expression
    '''
    phi = (1 + sqrt(5)) / 2
    return round(phi ** n / sqrt(5))


def main():
    '''
    Each new term in the Fibonacci sequence is generated by adding the previous
    two terms. By starting with 1 and 2, the first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    By considering the terms in the Fibonacci sequence whose values do not
    exceed four million, find the sum of the even-valued terms.
    '''
    result, n, fn = 0, 1, 0
    while fn <= 4e6:
        fn = fibonacci(n)
        if fn % 2 == 0:
            result += fn
        n += 1
    return result


if __name__ == '__main__':
    print(main())
