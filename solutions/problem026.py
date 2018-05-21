import math

def get_recurring_cycle_length(n):
	'''returns the length of the recurring cycle in `1/n`'''
	# `r` will be our remainder variable, which will begin at 1, as we are dividing 1 by the divisor `n`.
	r = 1

	# `zero_offset` will capture 0 the number of 0s in the cycle.
	# example of why this is necessary: 1 / 11
	zero_offset = 0

	# `remainders` will capture the remainders for each iteration.
	remainders = []

	# if `r` is 0, this means the remainder is 0 and division has come to an end, thus no recurring cycle exists.
	while r != 0:
		# we want the remainder from dividing `r` by `n`.
		_, r = divmod(r, n)

		# if we have seen the remainder before then we have found a cycle.
		if r in remainders:

			# the cycle length is the number of remainders we have gone through
			# less the index of the first time we saw this remainder.
			return len(remainders) - remainders.index(r) - 1 + zero_offset
		else:

			# having failed to find a cycle, we add the remainder to our list.
			remainders.extend([r])

			# we multiply `r` by the minimum power of 10 such that `n < r`.
			# this needs to be accounted for in the length of the recurring cycle.
			while 0 < r < n:
				zero_offset += 1
				r *= 10

	# if we reach this, `r` is 0, thus no cycle exists.
	return 0

def main():
	'''Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

	1/6	= 	0.1(6)
	1/7	= 	0.(142857)
	Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
	'''
	idx, val = 0, 0
	for i in range(2, 1000):
		cycle_length = get_recurring_cycle_length(i)
		if val < cycle_length:
			val = cycle_length
			idx = i

	return idx, val


if __name__ == '__main__':
	print(main())
