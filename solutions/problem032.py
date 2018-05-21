from itertools import permutations

def main():
	'''
	We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
	for example, the 5-digit number, 15234, is 1 through 5 pandigital.

	The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and
	product is 1 through 9 pandigital.

	Find the sum of all products whose multiplicand/multiplier/product identity can be written as a
	1 through 9 pandigital.
	'''

	# Two forms:
	# N x NNNN = NNNNN
	# NN x NNN = NNNN

	res = set()
	for p in permutations(['1', '2', '3', '4', '5', '6', '7', '8', '9'], 9):
		lhs, rhs = int(p[0]) * int(''.join(p[1:5])), int(''.join(p[5:]))
		if lhs == rhs:
			res.add(rhs)

		lhs, rhs = int(''.join(p[0:2])) * int(''.join(p[2:5])), int(''.join(p[5:]))
		if lhs == rhs:
			res.add(rhs)

	return(sum(res))



if __name__ == '__main__':
	print(main())
