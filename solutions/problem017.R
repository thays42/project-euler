## If the numbers 1 to 5 are written out in words: one, two, three, four, five,
## then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

## If all the numbers from 1 to 1000 (one thousand) inclusive were written out
## in words, how many letters would be used?

## NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
## forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
## letters. The use of "and" when writing out numbers is in compliance with
## British usage.
library(purrr)
library(stringr)

DIGITS <- c('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
TEENS <- c('eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen')
TENS <- c('ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety')

number_to_words <- function(x) {
    if (x == 1000) {
        return('onethousand')
    } else if (x %% 100 == 0) {
        hundreds <- x / 100
        return(paste0(DIGITS[hundreds], 'hundred'))
    } else if (x > 100) {
        hundreds <- x %/% 100
        tens <- x %% 100
        return(paste0(DIGITS[hundreds], 'hundredand', number_to_words(tens)))
    } else if (x %% 10 == 0) {
        tens <- x / 10
        return(TENS[tens])
    } else if (x > 20) {
        tens <- x %/% 10
        ones <- x %% 10
        return(paste0(TENS[tens], DIGITS[ones]))
    } else if (x > 10) {
        return(TEENS[x - 10])
    } else {
        return(DIGITS[x])
    }
}

map_chr(1:1000, number_to_words) %>%
    str_length() %>%
    sum()
