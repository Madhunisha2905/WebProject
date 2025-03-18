numbers = [23, 45, 12, 67, 34, 89, 2]
largest = max(numbers)
smallest = min(numbers)
print("Smallest number in the list:", smallest)
print("Largest number in the list:", largest)
total = sum(numbers)
print("Sum of elements in the list:", total)

# Count Occurrences of an Element in a List
fruits = ["apple", "banana", "apple", "orange", "apple"]
count_apple = fruits.count("apple")
print("Number of times 'apple' appears:", count_apple)

# Program to reverse a list
numbers = [1, 2, 3, 4, 5]
numbers.reverse()  # In-place reversal
print("Reversed list:", numbers)

# Program to remove duplicates from a list
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print("List after removing duplicates:", unique_numbers)

# Program to separate even and odd numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

# Program to sort a list in ascending and descending order
numbers = [42, 12, 56, 23, 78, 9]

numbers.sort()  # Ascending order
print("Ascending order:", numbers)

numbers.sort(reverse=True)  # Descending order
print("Descending order:", numbers)


# Program to find the second largest element in a list
numbers = [10, 20, 5, 25, 30]

numbers.sort()
print("Second largest element:", numbers[-2])


# Program to merge two lists without duplicates
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

merged_list = list(set(list1 + list2))
print("Merged list without duplicates:", merged_list)


# Program to find common elements in two lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common_elements = list(set(list1) & set(list2))
print("Common elements:", common_elements)

# Program to find intersection and union of two lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

intersection = list(set(list1) & set(list2))
union = list(set(list1) | set(list2))

print("Intersection:", intersection)
print("Union:", union)


# Program to create a list of squares
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]

print("Squares:", squares)