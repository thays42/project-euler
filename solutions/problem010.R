## The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

## Find the sum of all the primes below two million.
library(purrr)

is_prime <- function(x) {
    if (x == 1) {
        FALSE
    } else if (x < 4) {
        TRUE
    } else if (x %% 2 == 0) {
        FALSE
    } else if (x < 9) {
        TRUE
    } else if (x %% 3 == 0) {
        FALSE
    } else {
        r <- floor(sqrt(x))
        f <- 5
        while (f <= r) {
            if (x %% f == 0) return(FALSE)
            if (x %% (f + 2) == 0) return(FALSE)
            f <- f + 6
        }
        TRUE
    }
}

res <- 2
p <- 3
while (p < 2e6) {
    if (is_prime(p)) {
        res <- res + p
    }

    p <- p + 2
}
