def is_palindrome(s):
    '''
    Returns True if s is a palindrome, else False.
    '''
    s = str(s)
    return s == s[::-1]


def main():
    '''
    A palindromic number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is 9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
    '''
    return max([a*b
                for a in range(999, 99, -1)
                for b in range(999, a-1, -1)
                if is_palindrome(a*b)])


if __name__ == '__main__':
    print(main())
