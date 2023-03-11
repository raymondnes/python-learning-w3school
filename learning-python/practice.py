"""
print("Hello, World!")
if 5 < 2:
  print("Five is greater than two!")
else:
    print("two is less than five")
"""

"""
This is a multi line comment
wherein, stings not assigned to a variable
can be omitted and viewed as a comment by python
"""

# Creating Variable
"""
x = 5
y = "John"
print(x)
print(y)

this prints
5
john
"""

# Getting the type
# You can get the data type of a variable with the type() function.
"""
x = 28
y = "Raymond"
z = 3.14           #prints
print(type(x))    #<class 'int'>
print(type(y))    #<class 'int'>
print(type(z))    #<class 'float'>
"""

#VAriable Names
"""
It is important to always have a discriptive variable name, for clarity and collaborative ease.
Rules for Variable names are
Camel Case
myVarName - Capital first letter from the second word
Pascal Case
MyVariableName - capitalize the first letter of each word
Snake Case
my_variable_name - adding an underscore to each word 
"""
"""®
# Assigning Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#Assigning One Value to Multiple variables
x = y = z = "Orange"
print(x)
print(y)
print(z)
"""
#unpack a collection
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

"""
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
"""

# Global Variables
# These are variables created outside of a function and can be used inside the function
"""
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
"""