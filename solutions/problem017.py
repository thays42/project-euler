def number_word_length(n):
    '''
    Return the length of the number n written out
    Designed to work for numbers 1 ... 1000
    '''
    length = 0
    ones = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
    teens = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
    tens = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]

    if n == 1000:
        # add 11 for "one" and "thousand"
        return 11

    n_hundreds = n // 100
    n_tens = n % 100 // 10
    n_ones = n % 10

    if n_hundreds > 0:
        # add 7 for "hundreds"
        length += ones[n_hundreds] + 7
        if n_tens > 0 or n_ones > 0:
            # add 3 for "and"
            length += 3

    if n_tens > 1:
        length += tens[n_tens]
        length += ones[n_ones]
    elif n_tens == 1:
        length += teens[n_ones]
    else:
        length += ones[n_ones]

    return length

def main():
    '''
    If the numbers 1 to 5 are written out in words: one, two, three, four, five,
    then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

    If all the numbers from 1 to 1000 (one thousand) inclusive were written out
    in words, how many letters would be used?


    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
    forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
    letters. The use of "and" when writing out numbers is in compliance with
    British usage.
    '''
    return sum([number_word_length(x) for x in range(1, 1001)])


if __name__ == '__main__':
    print(main())
