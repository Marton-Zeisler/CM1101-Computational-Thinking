import unittest

def get_formatter_name(first, last, middle = ""):
	if middle:
		full_name = first + " " + middle + " " + last
	else:
		full_name = first + " " + last
	return full_name.title()


class NamesTestCase(unittest.TestCase):
	def setUp(self):
		# you can use this method to setup variables for your test methods
		self.first = "marci"
		self.last = "zeisler"
		self.middle = "peter"

	def test_name(self):
		formatted_name = get_formatter_name(self.first, self.last)
		self.assertEqual(formatted_name, "Marci Zeisler")

	def test_name_middle(self):
		formatted_name = get_formatter_name("marci", "zeisler", "peter")
		self.assertEqual(formatted_name, "Marci Peter Zeisler")


#unittest.main()

class hello:

	def __init__(self):
		self.hey = 10	

	def hello2(self):
		self.hey = "hey"
		print(self.hey)

	def hello3(self):
		print(self.hey)


h = hello()

h.hello2()
h.hello3()


