import Chapter8 # importing  module
import Chapter8 as ch8 # importing module and giving it an alias
from Chapter8 import hell, heyUser # importing specific functions
from Chapter8 import country as ctr # importing specific and renaming it
from Chapter8 import * # imports every function and call them without module

heyUser("marci") #calling a function when imported from specific function
ch8.hell() # calling functions from the imported module
ctr() # calls the function called country in Chapter8 module
print(martonName) # variables get imported too


