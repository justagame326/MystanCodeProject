"""
File: largest_digit.py
Name: Jerry
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: the input integer
	:return: max digit of the input integer
	"""
	n = abs(n)
	if n == 0:
		return n
	else:
		return max(n % 10, find_largest_digit(n//10))

	# return find_largest_digit_helper(n, n % 10)


def find_largest_digit_helper(n, current_largest_digit):
	if n/10 < 0.1:
		return current_largest_digit
	else:
		if n % 10 >= current_largest_digit:
			current_largest_digit = n % 10
		return find_largest_digit_helper(n//10, current_largest_digit)


if __name__ == '__main__':
	main()
