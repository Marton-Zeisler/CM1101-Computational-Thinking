import random

# 1
number = input("Enter a number: ")
if int(number) % 2 == 0:
	print("Even")
else:
	print("Odd")

# 2
# height = input("Enter the height: ")
# mass = input("Enter the mass")

# 3
numb1 = input("Enter first number: ")
numb2 = input("Enter second number: ")
numb3 = input("Enter third number: ")
first = int(numb1)
second = int(numb2)
third = int(numb3)

maximum = 0
if first > second and first > third:
	maximum = first

if second > first and second > third:
	maximum = second

if third > first and third > second:
	maximum = third

print("The maximum is " + str(maximum))
#print("Maximum is " + str(max(int(first),int(second), int(third))))


# 4
total = 0.0
counter = 0.0
answer = input("Enter a number: ")
while answer != "":
	total += float(answer)
	counter += 1
	answer = input("Enter a number: ")

print("The average is " + str(total / counter))

# 5
for bottles in range(99, 0, -2):
	print(str(bottles) + " bottles of beer on the wall, " + str(bottles) + " bottles of beer.\nTake one down, pass it around, " + str(bottles-1) + " bottles of beer on the wall.")

# 6
sentence = input("Enter a sentence: ")
letters = 0
digits = 0

for each in sentence:
	if each.isdigit():
		digits += 1
	if each.isalpha():
		letters += 1

print("Letters: " + str(letters))
print("Digits: " + str(digits))

# 7
randomNumber = random.randrange(1,11)
userGuess = 0
print("random " + str(randomNumber))
while userGuess != randomNumber:
	userGuess = int(input("Your guess? "))
	if userGuess == randomNumber:
		print("Correct")
		break
	if userGuess < randomNumber:
		print("Bigger")
	else:
		print("Smaller")

# 8
word = input("Enter a word: ")
if len(word) < 2:
	print(True)

middle = int(len(word)/2) - 1
wordCount = len(word)
answer = True
for each in range(0, middle):
	if word[each] != word[wordCount-1]:
		answer = False

print(answer)