## n! means n × (n − 1) × ... × 3 × 2 × 1

## For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,

## and the sum of the digits in the number 10! is
## 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

## Find the sum of the digits in the number 100!

# Interestingly, this is too complicated for R to do.
# It was able to handle 2 ** 1000...
options(scipen = 999)
factorial(100)

library(stringr)
library(magrittr)
library(Rmpfr) # more about this?

factorialMpfr(100) %>%
    coerce(character()) %>%
    str_split('', simplify = TRUE) %>%
    as.numeric() %>%
    sum()
