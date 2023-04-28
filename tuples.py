# Tuples are a collection of Python objects much like a list but Tuples are immutable in nature i.e. 
# the elements in the tuple cannot be added or removed once created.
# Tuples are more memory efficient than the lists. When it comes to the time efficiency, 
# tuples have a slight advantage over the lists especially when we consider lookup value. 
# If you have data that shouldn't change, you should choose tuple data type over lists.

my_tuple = (2, 8, 1, 6, 10)
print(my_tuple)

# Converting a list into a tuple
list = ["Hi", "my", "name", "is", "Carson"]
list = tuple(list)
print(list)