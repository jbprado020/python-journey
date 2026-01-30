# Python Functions
# A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.
# Example
def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))

# Python Function Arguments
# You can send data to functions as arguments. Python has several types of arguments:
# 1. Required arguments
def add(a, b):
    return a + b
print(add(5, 3))

# 2. Parameters vs Arguments
def my_function(name):
    print("Hello", name)

my_function("Emil")

# Number of Arguments
# By default, a function must be called with the correct number of arguments.

def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Emil", "Refsnes")

# Default Parameter Value

def my_function(name = "friend"):
    print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")

def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()

# Python *args and **kwargs
# *args is used to pass a variable number of non-keyword arguments to a function.

def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Tobias", "Linus", "Emil")

# using args with regular arguments

def my_function(age, *kids):
    print("The youngest child is " + kids[2] + " and age is " + str(age))