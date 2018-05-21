from math import floor

def weekday(year, month, day):
    '''
    https://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week#Disparate_variation
    For sanity, sane arguments will be accepted and then translated within this
    function.

    Month ranges 0 (January) to 11 (December)
    '''

    if month < 1:
        year -= 1
    c, y = year // 100, year % 100
    d = day
    m = month + 1 % 12
    return (d + floor(2.6 * m - 0.2) + y + floor(y / 4) + floor(c / 4) - 2 * c) % 7


def main():
    '''
    You are given the following information, but you may prefer to do some
    research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September, April, June and November.
    All the rest have thirty-one,
    Saving February alone, Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4,
    but not on a century unless it is divisible by 400.
    How many Sundays fell on the first of the month during the
    twentieth century (1 Jan 1901 to 31 Dec 2000)?
    '''

    return sum(weekday(y, m, 1) == 0 for y in range(1901, 2001)
                                     for m in range(12))

if __name__ == '__main__':
    print(main())
