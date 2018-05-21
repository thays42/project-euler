## A palindromic number reads the same both ways. The largest palindrome made
## from the product of two 2-digit numbers is 9009 = 91 × 99.

## Find the largest palindrome made from the product of two 3-digit numbers.
library(purrr)

is_palindrome <- function(x) {
    x <- as.character(x)
    x == stringi::stri_reverse(x)
}

problem4 <- function() {
    combn(100:999, 2, FUN = prod) %>%
        subset(is_palindrome(.)) %>%
        max()
}

problem4()
