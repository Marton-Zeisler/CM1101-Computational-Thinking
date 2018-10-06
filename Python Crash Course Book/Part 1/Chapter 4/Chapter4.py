names = ["Marci", "Peter", "David", "Balint"]

for each in names:
	print(each.lower())

for each in range(1,5):
	print(each, end=", ")

numbers = list(range(10,15))
print("\n")
print(numbers)

# incrementing by 2

for each in range(0,11,2):
	print(each)

print(10**2) # square in python

# statistics
print(min(numbers))
print(max(numbers))
print(sum(numbers))

squares = [value**2 for value in range(1,11)] # list comprehension
print(squares)

# slicing a list
s1 = squares[0:3] # copying items from index 0 to index 3 from other array
print(s1)

print(squares[-3:]) # printing last 3 items

# looping through a slice
for each in squares[:2]:
	print(each)

# copying a list
copy = squares[:] # without [:] it would only copy reference not values
print(copy)


# tuples
dimension = (200,50)
dimension = (100,20) # can't chance specific item, only whole tuple
print(dimension[0])
print(dimension[1])







