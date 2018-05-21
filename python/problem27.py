from problem7 import is_prime

def quadratic_formula(a, b):
	'''Generator for quadratic formula n ** 2 + a * n + b'''
	n = 0
	while True:
		yield n ** 2 + a * n + b
		n += 1

def main():
	'''Find the product of `a` and `b` such that:
	* `n^2 + an + b` is prime for the maximum consecutive values of `n`, starting at 0
	* `|a| < 1000` and `|b| <= 1000`
	'''

	# `b` must be prime in order for the equation to yield a prime for `n = 0`
	# `b` must be positive in order to yield a prime for `n = 0`
	# `a` must be odd in order to yield a possible prime
	# `a` must be at least -b + 1
	# if `a` is negative, we can short circuit if
	#    (best_n + 1) ** 2 + (best_n + 1) * a + b <= 1


	potential_a = [i for i in range(-999, 1001, 2)]
	potential_b = [i for i in range(3, 1001, 2) if is_prime(i)]

	best_n, best_a, best_b = 39, 1, 41

	for this_b in potential_b:
		for this_a in (x for x in potential_a if x > -this_b):
			this_n = 0

			if (best_n + 1) ** 2 + (best_n + 1) * this_a + this_b <= 1:
				continue

			f = quadratic_formula(this_a, this_b)
			while f is not None:
				next_f = next(f)
				if next_f > 0 and is_prime(next_f):
					this_n += 1
				else:
					if best_n < this_n:
						best_n = this_n
						best_a = this_a
						best_b = this_b
					f = None

	return(best_n, best_a, best_b, best_a * best_b)


if __name__ == '__main__':
	print(main2())
