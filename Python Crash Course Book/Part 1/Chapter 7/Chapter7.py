# inputs
message = input("Enter your name: ")
print(message)
age = int(input("Enter your age: "))
#age = int(age)
if age >= 18:
	print("You can drink")
else:
	print("You can't drink")

if age % 2 == 0:
	print("even")
else:
	print("odd")


# while loops
count = 10
while count >= 0:
	print(count)
	count -= 1

print("Repeating until you say \"exit\"")
message = ""
while message != "exit":
	message = input("")
	if message != "exit":
		print(message)

numbers = [1,2,3,4,5]
while numbers: # loops while array is not empty
	print(numbers)
	numbers.pop()

numbers = ["marci", "david", "peter", "balint"]
while "david" in numbers: # looping through while element is inside the array
	numbers.pop()

print(numbers)