## By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
## that the 6th prime is 13.

## What is the 10 001st prime number?
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

i <- 2
p <- 3
q <- 5
while (i < 10001) {
    if (is_prime(q)) {
        p <- q
        i <- i + 1
    }
    q <- q + 2
}
