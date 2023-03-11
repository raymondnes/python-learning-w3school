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

# Create a variable inside a function, with the same name as the global variable
"""
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()
print("Python is " + x)

prints
Python is fantastic
Python is awesome

"""
# If you use the global keyword, the variable belongs to the global scope:
"""
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

prints
Python is fantastic
"""

# Change the global keyword
# Also, use the global keyword if you want to change a global variable inside a function.
# To change the value of a global variable inside a function, refer to the variable by using the global keyword:

"""
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

prints
Python is fantastic

"""

# Python Data types

"""
Example	                                              Data Type
x = "Hello World"	                                     str	
x = 20	                                                 int	
x = 20.5	                                            float	
x = 1j                                                 complex	
x = ["apple", "banana", "cherry"]	                    list	
x = ("apple", "banana", "cherry")                       tuple	
x = range(6)	                                        range	
x = {"name" : "John", "age" : 36}           	        dict	
x = {"apple", "banana", "cherry"}	                    set	
x = frozenset({"apple", "banana", "cherry"})         frozenset	
x = True	                                            bool	
x = b"Hello"	                                       bytes	
x = bytearray(5)	                                 bytearray	
x = memoryview(bytes(5))                             memoryview	
x = None	                                          NoneType	

"""

#Specifying the Data types

"""
x = str("Hello World")	                                str	
x = int(20)	                                            int	
x = float(20.5)	                                        float	
x = complex(1j)	                                        complex	
x = list(("apple", "banana", "cherry"))	                list	
x = tuple(("apple", "banana", "cherry"))	            tuple	
x = range(6)	                                        range	
x = dict(name="John", age=36)	                        dict	
x = set(("apple", "banana", "cherry"))	                set	
x = frozenset(("apple", "banana", "cherry"))	        frozenset	
x = bool(5)	                                            bool	
x = bytes(5)	                                        bytes	
x = bytearray(5)	                                    bytearray	
x = memoryview(bytes(5))	                            memoryview
"""