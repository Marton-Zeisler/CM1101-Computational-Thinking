number = 111

if number % 2 == 0:
	print("even")
elif number % 2 != 0:
	print("odd")


# Recursion

def countdown(n):
	if n == 0:
		print("the end")
	else:
		print(str(n) + "...")
		countdown(n-1)

countdown(10)

# input
name = input("What's your name? ")
print("Nice to see you Mr. " + name)

