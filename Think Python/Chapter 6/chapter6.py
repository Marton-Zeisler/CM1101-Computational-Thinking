# return values

def add(a,b):
	return a + b

print(add(10,20))

# more recursion
def factorial(n):
	if n == 0:
		return 1
	else:
		return factorial(n-1) * n

print(factorial(4))

def fib(n):
	if not isinstance(n, int): # ! means not in python
		print("Fib only works with integers")
		return None
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

print(fib(4))














