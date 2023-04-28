# A dictionary is like hash tables in any other language with the time complexity of O(1). 
# It is an unordered collection of data values, used to store data values like a map, which, 
# unlike other Data Types that hold only a single value as an element, Dictionary holds the key:value pair. 
# Key-value is provided in the dictionary to make it more optimized.

dictionary = {
    "key": "value",
    "key2": "another value"
}

# Grabbing values from the dictionary
print(dictionary["key"])

# Traversing through a dictionary
print("\n")
for item in dictionary:
    print(dictionary[item])

# There is a better way to grab values from a dictionary that avoids possible key errors
print("\n")
print(dictionary.get("key"))