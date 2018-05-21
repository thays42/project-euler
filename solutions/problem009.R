## A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

## a2 + b2 = c2
## For example, 32 + 42 = 9 + 16 = 25 = 52.

## There exists exactly one Pythagorean triplet for which a + b + c = 1000.
## Find the product abc.

# Slower R-esque solution
res <- combn(1:500, 2, function(x) {
    z <- 1000 - sum(x)

    if (sum(x ** 2) == (z ** 2)) {
        prod(c(x, z))
    } else {
        0
    }
}) %>% max()

# Faster, straightforward solution
best <- 0
for (x in 500:1) {
    for (y in 2:x) {
        z <- 1000 - x - y
        if ((x ** 2 + y ** 2) == (z ** 2)) {
            best <- max(best, x * y * z)
        }
    }
}
