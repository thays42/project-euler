## By starting at the top of the triangle below and moving to adjacent numbers
## on the row below, the maximum total from top to bottom is 23.

## 3
## 7 4
## 2 4 6
## 8 5 9 3

## That is, 3 + 7 + 4 + 9 = 23.

## Find the maximum total from top to bottom of the triangle below:
library(stringr)
library(purrr)

parse_input <- function(x) {
    x %>%
        str_split(" ") %>%
        map(as.numeric)
}

find_best_path <- function(tri) {
    for (i in length(tri):2) {
        this_row <- tri[[i]]
        best_of_row <- map_dbl(1:(i - 1), ~ max(this_row[.x], this_row[.x + 1]))
        tri[[i - 1]] <- tri[[i - 1]] + best_of_row
    }

    tri[[1]]
}

tri18 <- readLines("inputs/p018_triangle.txt") %>%
    parse_input() %>%
    find_best_path()

tri67 <- readLines("inputs/p067_triangle.txt") %>%
    parse_input() %>%
    find_best_path()
