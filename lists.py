# A list is a collection of values that can be indexed
list = [1, 5, 2, 9, 7]
print("List output:")

# Iterating through the list and printing each value
for item in list:
    print(str(item))

# Grabbing a spcific value from the list
print("\nValue of the first item in the list:")
print(list[0])

# Using conditions to check values in the list
largest = 0
for item in list:
    if item > largest:
        largest = item

print("\nLargest value in list:")
print(largest)

# Adding values to the list
print("\n Adding '6' to the list")
list.append(6)
print(list)

# Taking values away from the list
print("\n Taking '6' away from the list")
list.pop()
print(list)

# You can specify the index of the value when using the pop method
print("\n Taking '6' away from the list")
list.pop(3)
print(list)