## 2520 is the smallest number that can be divided by each of the numbers from 1
## to 10 without any remainder.

## What is the smallest positive number that is evenly divisible by all of the
## numbers from 1 to 20?

# This is equal to taking the products of primes less than or equal to 20, each
# taken to the highest power it appears as a prime factor for the numbers 1 to 20.

problem5 <- (2 ** 4) * (3 ** 2) * 5 * 7 * 11 * 13 * 17 * 19

library(purrr)
library(dplyr)
prime_factors <- function(x) {
    # the product of the first 15 primes is 614,889,782,588,491,392, bigger than
    # i expect to deal with, so we will set that as our limit
    if (x > 6.148898e+17) {
        stop("Input `x` is too big for this function to handle.")
    }

    primes <- numeric(15)
    powers <- numeric(15)
    nth <- 1L

    i <- 2
    while(i <= floor(sqrt(x))) {
        if (x %% i == 0) {
            primes[nth] <- i
            powers[nth] <- 1
            x <- x / i

            while (x %% i == 0) {
                powers[nth] <- powers[nth] + 1
                x <- x / i
            }

            nth <- nth + 1
        }

        i <- ifelse(i == 2, 3, i + 2)
    }

    if (x > 1) {
        primes[nth] <- x
        powers[nth] <- 1
    }

    list(primes = keep(primes, ~ . > 0),
         powers = keep(powers, ~ . > 0))
}

problem5.general <- function(lo, hi) {
    map_df(lo:hi, prime_factors) %>%
        group_by(primes) %>%
        summarize(powers = max(powers)) %>%
        mutate(expn = primes ** powers) %>%
        pull(expn) %>%
        prod()
}

