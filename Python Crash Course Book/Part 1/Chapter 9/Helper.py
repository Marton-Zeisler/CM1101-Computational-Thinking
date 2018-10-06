from Chapter9 import Dog #import Dog # importing a single calss
from collections import OrderedDict # importing a class from Standard Library

sunny = Dog("sun", 20)
sunny.sit()

names = OrderedDict() # keeps the order of added key-value pairs
names["Marci"] = 20
names["David"] = 30
names["Mariann"] = 40

for name, age in names.items():
	print(name + " " + str(age) + " years old!")



