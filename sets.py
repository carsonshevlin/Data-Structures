#A Set in Python programming is an unordered collection data type that is iterable, mutable and has no duplicate elements. 
#The major advantage of using a set, as opposed to a list, is that it has a highly optimized method for checking whether a specific element is contained in the set. 
#This is based on a data structure known as a hash table. Since sets are unordered, we cannot access items using indexes as we do in lists.
myset = {"Geeks", "for", "Geeks"}
print(myset)

#Example: Check if an element is present in a set
data = {7058, 7059, 7072, 7074, 7076}
# check 7058
print(7058 in data)