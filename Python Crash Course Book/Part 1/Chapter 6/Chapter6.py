me = {} # creating an empty dictionary/clearing all elements
me = {"eyes": "brown", "name": "Marci", "city": "Budapest", "age": 20}
print(me["age"])
me[20] = 200 # adding a new key value pair / modifying an already existing pair in the dictionay
print(me[20])
del me["eyes"] # removing a pair in the dictionary

for key, value in me.items(): # looping through the kyes and values at the same time
	print("key: " + str(key) + " , value: " + str(value))

for key in me.keys(): # looping through the keys only, same thing as for each in keys:
	print(key)

for value in me.values(): # looping through the values only
	print(value)

# dictionaries are not sorted, if you need a sorted list of the keys use sorted()
del me[20] # sorting only works witj one data type, so make sure all the keys are one type
keys = sorted(me.keys())
print(keys)

# dictionries often have duplicates, to remove them as you loop through the values
# just make a set of the values then loop through them
me["duplicate"] = "Budapest"
for value in set(me.values()): # a set doesn not hold any duplicates
	print("hey " + str(value))


# list of dictionaries
print("list of dictionaries")
dicts = [{"name": "Marci"}, {"name": "Balint"}, {"name": "Peter"}]
for each in dicts:
	for key, value in each.items():
		print(key + " " + value)

for each in range(2):
	dicts.append({"name": str(each)})

for each in dicts[3:]:
	print(each)



# a list in a dictionary
print("a list in a dictionary")
pizza = {"crust": "thick", "toppings": ["mushrooms", "cheese"]}
for key,value in pizza.items():
	if key == "toppings":
		print("You ordered the following toppings: ", end="")
		for each in value:
			print(each, end=", ")
	else:
		print(key)




# a dictionary in a dictionary
print("\na dictionary in a dictionary")
users = {"123122": {"first": "Marci", "last": "Zeisler", "gender": "male"}}

for key, value in users.items():
	print("username: " + key)
	print("first name: " + value["first"])
	print("last name " +  value["last"])
	print("gender " + value["gender"])























