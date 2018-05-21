from math import log, sqrt

def main():
    '''
    What is the index of the first term in the Fibonacci sequence to contain
    1000 digits?

    Answer:

    - The first term to contain 1000 digits will be greater than 10^999
    - The nth Fibonacci number is the nearest integer of:
        phi^n / sqrt(5)
    - Thus, we want n such that:
        phi^n / sqrt(5) > 10^999
    - Take the natural log of both sides:
        ln(phi^n / sqrt(5)) > ln(10^999)
   n * ln(phi) - ln(5) / 2 > 999 * ln(10)
                n * ln(phi) > 999 * ln(10) + ln(5) / 2
                           n > (999 * ln(10) + ln(5) / 2) / ln(phi)
    - Thus, the least whole number value for n satisfying the equality is:
    '''

    phi = (1 + sqrt(5)) / 2
    return round((999 * log(10) + log(5) / 2) / log(phi))

if __name__ == '__main__':
    print(main())
