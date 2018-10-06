names = ["Marci", "David", "Vicky"]
print(names[1])
names[0] = "marci"

names.append("cicu") # adding an element at the end
names.insert(3, "Mariann") # inserting element at given index
print("Last item is " + names[-1]) # accessing last element
print(names[-2]) # second last item

del names[0] # removes an element at a given index
print(names)

print(names.pop()) # removes and returns last element
print(names.pop(0)) # removes and returns element at given index

names.remove("Mariann") # removes specific element
print(names)

numbers = [2,3,1,5,3,55,10,22,9]
numbers.sort() # sorts list in ascending order
print(numbers)
numbers.sort(reverse=True)
print(numbers) # sorts list in descending order

print(sorted(numbers)) # returns but not modifies the sorted list in ascending order
print(numbers)

names.append("Balint")
names.sort()
names.reverse() # reverses the current list order
print(names)

print(len(numbers)) # returns the number of elements in the list







