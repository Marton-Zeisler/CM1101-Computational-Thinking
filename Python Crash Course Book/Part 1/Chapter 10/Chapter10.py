import json
# we need to first open the text file
# the open functions needs a name of file parameter
# with keyword closes the file once access to it is no longer needed
# you could close the file manually too but if a bug in your program prevents the close() call, file may suffer from data loss
# file within folder: "files/digits.txt"
with open("pi_digits.txt") as file_object:
	contents = file_object.read()
	print(contents)

# reading line by line
print("\nreading line by line\n")
with open("pi_digits.txt") as file_object:
	for line in file_object:
		print(line.rstrip())

# making a list of lines from a file
print("\nmaking a list of lines from a file\n")
with open("pi_digits.txt") as file_object:
	lines = file_object.readlines()

print(lines[0])

# writing to an empty file
with open("name.txt", "w") as file_object:
	file_object.write("Marton Zeisler\nCardiff\n")

# writing multiple lines
# the write() function doesn't add new new lines to the text you write
# so use the \n to make a new line

# appending to a file - not erasing the file
with open("name2.txt", "a") as file_object:
	file_object.write("Appended again damn it\n")

# exceptions - try-except
# for exmaple, python can't handle zero division
try:
	print(5/0)
except ZeroDivisionError:
	pass # pass means do nothing just move on
	#print("You can't divide by zero!")


# also good idea to put file readings in try except block

try:
	with open("book.txt") as file_object:
		contents = file_object.read()
except: #FileNotFoundError
	print("Sorry, file not found")
else: # this code will only run if try was successful
	words = len(contents.split())
	print("The file contains this many words: " + str(words))


# writing json
# json.dump() - two arguments, data to store and file object it can use to store the data
numbers = [10,20,30,40,50]

try:
	with open("json.json") as file_object:
		loadedNumbers = json.load(file_object)
except FileNotFoundError:
	with open("json.json", "w") as file_object:
		json.dump(numbers, file_object)
		print("saved josh don't worry")
else:
	print(loadedNumbers)








