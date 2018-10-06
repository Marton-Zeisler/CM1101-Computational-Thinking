class Dog():
	# A function that's part of a class is a method
	def __init__(self, name, age):
		# __init__() is a special method Python runs automatically whenever we
		# create a new instance based on the Dog class
		# This method has 2 leading underscores and two trailing underscores
		#, a convention that helps Python's default method names from
		# conflicting with your method name
		# the self parameter is required in the method definition and
		# it must come first before the other parameters		
		self.name = name
		self.age = age
		self.pet = "dog" # setting default value for an attribute
		# any variable prefixed with self. is available to every method
		# in the class, and can be accessed through the instance
	def sit(self):
		print(self.name + " is sitting!")

	def setName(self, name):
		self.name = name

	def getDescription(self):
		return self.name + " is " + str(self.age) + " years old " + self.pet


myDog = Dog("Sunny", 4)
myDog.age = 3
myDog.setName("Cicu")
myDog.sit()
print(myDog.getDescription())

# Inheritence
class Puppy(Dog): # inherits all the methods and variables
	def __init__(self, name, age):
		super().__init__(name, age)
		self.newBorn = False

	def isNewBorn(self):
		return self.newBorn

	def sit(self): # overriding method from the parent class
		print("puppy cannot sit too cute")

myPuppy = Puppy("puppy", 1)
print(myPuppy.getDescription())
myPuppy.sit()
myPuppy.newBorn = True
if myPuppy.isNewBorn():
	print("yes, new born")
else:
	print("nope, not new born")






































