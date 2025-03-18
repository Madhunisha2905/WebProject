# Accessing tuple elements
fruits = ("apple", "banana", "orange")

print("First element:", fruits[0])      
print("Last element:", fruits[-1])       
print("Slice of tuple:", fruits[1:3])   

# Length of a tuple
numbers = (1, 2, 3, 4, 5, 2, 5, 6, 5, 5, 5, 2, 5, 2)
print("Length of the tuple:", len(numbers))
print("Occurrences of 2:", numbers.count(5))
my_list = list(numbers)
print("Converted list:", my_list)
print("Maximum value:", max(numbers))
print("Minimum value:", min(numbers))
print("Sum of elements:", sum(numbers))

# Merging two tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged_tuple = tuple1 + tuple2
print("Merged tuple:", merged_tuple)

# Repeating tuple elements
my_tuple = ("Hi",) * 3
print("Repeated tuple:", my_tuple)

# Checking for element existence
fruits = ("apple", "banana", "cherry")

if "apple" in fruits:
    print("Apple is in the tuple")
else:
    print("Apple is not in the tuple")

# Iterating through a tuple
colors = ("red", "green", "blue")

for color in colors:
    print(color)

# Checking if a tuple is empty
empty_tuple = ()

if not empty_tuple:
    print("The tuple is empty.")
else:
    print("The tuple is not empty.")