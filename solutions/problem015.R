## Starting in the top left corner of a 2×2 grid, and only being able to move to
## the right and down, there are exactly 6 routes to the bottom right corner.

## How many such routes are there through a 20×20 grid?

# We have to travel across 40 lines
# 20 moves must be vertical, the other 20 must be horizontal
# This is equivalent to determining how many ways to write a
# 40-bit string with 20 1s and 20 0s, which is calculated
# as "40 choose 20".
choose(40, 20)
