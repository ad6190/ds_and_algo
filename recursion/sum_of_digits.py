import random

def sum_of_digits(n):
	return (n % 10) + sum_of_digits(n/10) if n/10 != 0 else n


if __name__ == "__main__":
	n = random.randrange(10, 5000)
	print(n, "sum of digits", sum_of_digits(n))