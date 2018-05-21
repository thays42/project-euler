from math import floor

def main():
	'''In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
	    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

		It is possible to make £2 in the following way:
	    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

	    How many different ways can £2 be made using any number of coins?
	'''

	# asked another way... how many combinations of (a, b, c, d, e, f, g, h) satisfy:
	# a + 2b + 5c + 10d + 20e + 50f + 100g + 200h = 200

	# for each term with coefficient c_i and variable x_i, with target t = 200
	# x_i can take values in the range 0 <= x_i <= t / c_i
	# cnt = 0
	# for a in range(201):
	# 	for b in range(101):
	# 		for c in range(41):
	# 			for d in range(21):
	# 				for e in range(11):
	# 					for f in range(5):
	# 						for g in range(3):
	# 							for h in range(2):
	# 								if a + b * 2 + c * 5 + d * 10 + e * 20 + f * 50 + g * 100 + h * 200 == 200:
	# 									cnt += 1

	# the above searches all possible values of each term, which will lead to a number of combinations over the target
	# we can limit this
	def valid_range(target, coefficient, offset):
		return range(floor((target - offset) / coefficient) + 1)

	return sum([1
				for a in range(201)
				for b in valid_range(200, 2, a)
				for c in valid_range(200, 5, a + b * 2)
				for d in valid_range(200, 10, a + b * 2 + c * 5)
				for e in valid_range(200, 20, a + b * 2 + c * 5 + d * 10)
				for f in valid_range(200, 50, a + b * 2 + c * 5 + d * 10 + e * 20)
				for g in valid_range(200, 100, a + b * 2 + c * 5 + d * 10 + e * 20 + f * 50)
				if a + b * 2 + c * 5 + d * 10 + e * 20 + f * 50 + g * 100 == 200]) + 1


if __name__ == '__main__':
	print(main())
