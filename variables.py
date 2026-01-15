#####  Variable Examples   

# This file contains examples of different types of variables in Python.

# You can modify the values to see how they work.

# Integer variable
age = 20

# Float variable
height = 5.4

# String variable
name = "Julianne"

# Boolean variable
is_Learning = True
is_NotLearning = False

# Collection List, Tuple, Sets, Dictionary

stuff = ["Books", "Laptop", "Pen"]
things = ("Mouse", "Keyboard", "Monitor")
items = {"Table", "Chair", "Lamp"}
details = {"Name": "Julianne", "Age": 20, "Height": 5.4}

# Global variables

x = "Student"

def function():
    print("Julianne is a " + x)
function()

# Global variables using 'global' keyword

def another_function():
    global y
    y = "Developer"
another_function()
print("Julianne is a " + y)
