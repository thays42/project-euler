## The prime factors of 13195 are 5, 7, 13 and 29.

## What is the largest prime factor of the number 600851475143 ?

library(purrr)
is_prime <- function(x) {
    if (x == 2) {
        return(TRUE)
    } else if (x %% 2 == 0) {
        return(FALSE)
    } else {
        seq(3, floor(sqrt(x)), by = 2) %>%
            detect(~ x %% . == 0) %>%
            is.null()
    }
}

largest_prime_factor <- function(x) {
    while (x %% 2 == 0) {
        x <- x / 2
    }

    if (x == 1) {
        2
    } else {
        seq(3, floor(sqrt(x)), by = 2) %>%
            detect(~ x %% . == 0 && is_prime(.), .right = TRUE)
    }
}

problem3 <- function() {
    largest_prime_factor(600851475143)
}

problem3()
