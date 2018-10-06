cars = ["audi", "bmw", "subaru"]

for each in cars:
	if each == "bmw":
		print(each.upper())

if "me" != "me".upper():
	print("different")

age = 20

if age >= 18 and age <= 30:
	print("drink and stay young")

if age < 18 or age > 80:
	print("Try not to drink")


if "audi" in cars: # checking if item is part of the list
	print("You've got an audi")

if "ferrari" not in cars: # checking if item is not part of the list
	print("Gott get a ferrari soon")

if ("Porsche" in cars) == False: 
	print("Buy Porsche soon too pls")

if age >= 21:
	print("you can drink in America")
elif age == 20: # else if in Python
	print("You can drink next year")
else:
	print("gotta wait " + str(21-age) + " years")

list = []
if list:
	print("List is not empty")

if not list:
	print("List is empty: " + str(len(list)))


