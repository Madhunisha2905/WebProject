# Adding elements to a set
numbers = {1, 2, 3}
numbers.add(4)
print("Updated set:", numbers)
numbers.remove(3) 
print("After removing 3:", numbers)
numbers.discard(10)  # No error even if 10 is not in the set
print("After trying to remove 10:", numbers)

# Checking membership
print(2 in numbers)    
print(5 in numbers) 

# Union & intersection of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print("Union of sets:", union_set)
intersection_set = set1.intersection(set2)
print("Intersection of sets:", intersection_set)

# Difference of two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}
difference_set = set1.difference(set2)
print("Difference of sets:", difference_set)


