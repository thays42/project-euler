## You are given the following information, but you may prefer to do some research for yourself.

## 1 Jan 1900 was a Monday.
## Thirty days has September,
## April, June and November.
## All the rest have thirty-one,
## Saving February alone,
## Which has twenty-eight, rain or shine.
## And on leap years, twenty-nine.

## A leap year occurs on any year evenly divisible by 4, but not on a century
## unless it is divisible by 400.

## How many Sundays fell on the first of the month during the twentieth century
## (1 Jan 1901 to 31 Dec 2000)?

# we can use packages to do this very easily
library(lubridate)
library(purrr)

seq(ymd('1901-01-01'), ymd('2000-12-31'), by = '1 month') %>%
    lubridate::wday() %>%
    keep(~ . == 1) %>%
    length()

# we can also use math!
# http://mathforum.org/dr.math/faq/faq.calendar.html
day_of_week <- function(y, m, d) {
    k <- d
    m <- ((m - 3) %% 12) + 1
    if (m > 10) {
        y <- y - 1
    }
    D <- y %% 100
    C <- y %/% 100

    res <- k + floor((13 * m - 1) / 5) + D + floor(D/4) + floor(C/4) - 2 * C
    res %% 7
}

expand.grid(y = 1901:2000, m = 1:12) %>%
    pmap_dbl(day_of_week, d = 1) %>%
    keep(~ . == 0) %>%
    length()
