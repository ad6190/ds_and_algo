
def factorial(n):
	return n * factorial(n-1) if n > 1 else 1


if __name__ == "__main__":
	n = 10
	if n < 0 :
		print("invalid input") 
		exit()
	print(factorial(n))
	n = 0
	if n < 0 :
		print("invalid input") 
		exit()
	print(factorial(n))
	n = 5
	if n < 0 :
		print("invalid input") 
		exit()
	print(factorial(n))
	n = -1
	if n < 0 :
		print("invalid input")
		exit()  
	print(factorial(n))