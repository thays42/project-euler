def main():
	'''Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.'''

	# 9 ** 5 = 59,049
	# (9 ** 5) * 6 = 354,294, making this a ceiling for potential numbers
	def sum_of_fifth_power_digits(i):
		return sum(pow(int(d), 5) for d in str(i))

	return sum(i for i in range(2, 354294) if sum_of_fifth_power_digits(i) == i)

if __name__ == '__main__':
	print(main())
