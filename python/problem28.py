def main():
	'''Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

		21 22 23 24 25
		20  7  8  9 10
		19  6  1  2 11
		18  5  4  3 12
		17 16 15 14 13

		It can be verified that the sum of the numbers on the diagonals is 101.

		What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
	'''

	# starting at the center and going up and right, we get a series of squares of odd integers: 1, 9, 25, ...
	# the ith odd square can be expressed as ((2 * i) + 1) ** 2
	def odd_square(i):
		return ((2 * i) + 1) ** 2

	# starting at the middle, we are dealing with concentric squares, the corners of which are:
	# 3, 5, 7, 9 (= 3 * 3 aka 2nd odd squared)
	# 13, 17, 21, 25 (= 5 * 5 aka 3rd odd squares)
	# the ith concentric square has a step size of 2 * i, the ith even number
	# the terms can then be expressed in terms of the ith odd squares and the ith even number.
	# 3 = 9 - (2 * 3), 5 = 9 - (2 * 2), 7 = 9 - (2 * 1)
	# the sum is then 4 * 9 - 2 * 6
	# the ith concentric square diagonals will sum to 4 * (ith odd square) - (ith even number) * 6
	# the 0th concentric square is the center, i.e. 1
	def diagonal_sum(i):
		if i == 0:
			return 1
		else:
			return 4 * odd_square(i) - (2 * i) * 6

	# a 1001 by 1001 spiral is made of 500 concentric squares and the center:
	return sum(diagonal_sum(i) for i in range(501))

if __name__ == '__main__':
	print(main())
