# Python Tuples
# A tuple is a collection which is ordered and unchangeable. In Python, tuples are written with round brackets.

# Creating a Tuple
my_tuple = ("apple", "banana", "cherry")
print(my_tuple)

# Duplicate Values
my_tuple = ("apple", "banana", "cherry", "apple", "cherry")
print(my_tuple)

# Tuple Length
print(len(my_tuple))

# Creating Tuples With One Item
single_item_tuple = ("apple",)  # Note the comma
print(single_item_tuple)

# Tuple Items - Data Types

tuple_mixed = ("apple", 42, True, 3.14)
print(tuple_mixed)

# Tuple Constructor

tuple_from_constructor = tuple(("apple", "banana", "cherry"))
print(tuple_from_constructor)

# Python Collections (Arrays)

# There are four collection data types in the Python programming language:
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is ordered* and changeable. No duplicate members.

# Python Access Tuple Items
# You can access tuple items by referring to the index number, inside square brackets.

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])  # Accessing the second item

# Negative Indexing
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])  # Accessing the last item

# Range of Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])  # From index 2 to 4

# Range of Negative Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])  # From index -4 to -2

# Check if Item Exists
thistuple = ("apple", "banana", "cherry")
if "banana" in thistuple:
    print("Yes, 'banana' is in the tuple")

# Update Tuples
# Tuples are unchangeable, but you can convert it to a list, change the list, and convert it back to a tuple.

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y[1] = "kiwi"
thistuple = tuple(y)
print(thistuple)

# Add Items
# Since tuples are unchangeable, you cannot add items to it. But you can convert it to a list, add the item, and convert it back to a tuple.

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

# Remove Items

# Tuples are unchangeable, so you cannot remove items from it. But you can convert it to a list, remove the item, and convert it back to a tuple.

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("banana")
thistuple = tuple(y)

# Unpack Tuples

thistuple = ("apple", "banana", "cherry")
(green, yellow, red) = thistuple

print(green)
print(yellow)
print(red)

# Using Asterisk*
# If the number of variables is less than the number of values, you can add an asterisk* to the variable name and the values will be assigned to the variable as a list.

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
(green, yellow, *red) = thistuple
print(green)
print(yellow)
print(red)

# Loop Through a Tuple

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)
