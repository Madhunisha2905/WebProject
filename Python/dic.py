# Adding new key-value pairs
person = {"name": "Madhunisha"}
person["age"] = 24  
person["city"] = "Trichy"

print("Updated Dictionary:", person)

# Removing elements
student = {"name": "Madhu", "age": 24, "course": "Math"}
student.pop("age")          # Removes a specific key
print("After pop:", student)

del student["course"]       # Deletes a key
print("After del:", student)

student.clear()             # Clears the entire dictionary
print("After clear:", student)

# Iterating through keys and values
employee = {"name": "Jane", "role": "Developer", "salary": 50000}

for key, value in employee.items():
    print(f"{key}: {value}")


# Checking for key existence
car = {"brand": "Toyota", "model": "Corolla", "year": 2022}

if "model" in car:
    print("Model is available!")
else:
    print("Model is not available.")

# Merging dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged_dict = {**dict1, **dict2}
print("Merged Dictionary:", merged_dict)


# Word frequency counter
text = "madhu nisha madhu hari nisha madhu"

word_count = {}
for word in text.split():
    word_count[word] = word_count.get(word, 0) + 1

print("Word Frequency:", word_count)


# Creating dictionary from two lists
keys = ["name", "age", "city"]
values = ["John", 30, "New York"]
person = dict(zip(keys, values))
print("Dictionary:", person)

# Swapping keys and values
original = {"a": 1, "b": 2, "c": 3}
reversed_dict = {value: key for key, value in original.items()}

print("Reversed Dictionary:", reversed_dict)