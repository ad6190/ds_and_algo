import random 

def factorial(n):
	return n * factorial(n-1) if n > 1 else 1


if __name__ == "__main__":
	n = random.randrange(-10, 10)
	print(n)
	if n < 0 :
		print("invalid input") 
		exit()
	print(factorial(n))
	