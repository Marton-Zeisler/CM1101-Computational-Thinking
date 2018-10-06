martonName = "Marton cicu"
def hell():
	print("Hello there")

def heyUser(name):
	print("Welcome " + name)

def myPets(pet1, pet2):
	print("I have a " + pet1)
	print("And a " + pet2)

#myPets("dog", "cicu")
myPets(pet2="doggy", pet1="cicu") # using keyword arguments, order can be changed

def country(name = "UK"): # default values
	print("Welcome to " + name)

country()

# return values
def hey():
	return "returning hey"

print(hey())

def name(first, last, middle=""): # optional parameter - must be last one
	if middle: # non-empty strings are considered true
		print("you gave middle name")
	else:
		print("no middle name was given")

name("marci", "zeisler")

# functions can return arrays and even dictionaries too
def build():
	return {"marci": 20, "vicky": 23}

print(build()["marci"])


#modifying a list in a function
numbers = [1,2,3]
def times10(numbers):
	for each in range(0,len(numbers)):
		numbers[each] *= 10
times10(numbers)
print(numbers)



# preventing a function from modifying a list
def add100(numbers):
	for each in range(0, len(numbers)):
		numbers[each] += 100
add100(numbers[:]) # this will tell the function to make a copy and modify the copy itself not the original data
print(numbers) # remains untouched

# passing an arbitrary number of arguments
def pizza(*toppings): # it will place them in a tuple
	for each in toppings:
		print(each + "? Got that sir! ")

pizza("Mushroom", "pepperoni", "extra cheese")

# mixing positional and arbitrary arguments
# if you want different kinds of arguments, place the arbitrary at the end
def pizza2(number, *toppings):
	for each in range(0, len(toppings)):
		print(toppings[each])

pizza2(2, "sauce", "garlic")

# accepting as many key-value paris as caller provides
def build_profile(first, last, **user_info):
	profile = {}
	profile["first"] = first
	profile["last"] = last
	for key,value in user_info.items():
		profile[key] = value
	return profile

user = build_profile("marci", "zeisler", country="UK", age=20)
print(user)




















