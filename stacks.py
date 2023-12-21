#Stack is a linear data structure that follows a particular order in which the operations are performed. The order may be LIFO(Last In First Out) or FILO(First In Last Out). 
#LIFO implies that the element that is inserted last, comes out first and FILO implies that the element that is inserted first, comes out last.

#The functions associated with stack are:

#empty() – Returns whether the stack is empty – Time Complexity: O(1)
#size() – Returns the size of the stack – Time Complexity: O(1)
#top() / peek() – Returns a reference to the topmost element of the stack – Time Complexity: O(1)
#push(a) – Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)
#pop() – Deletes the topmost element of the stack – Time Complexity: O(1)

# Python program to
# demonstrate stack implementation
# using list
stack = []
 
# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')
 
print('Initial stack')
print(stack)
 
# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
 
print('\nStack after elements are popped:')
print(stack)

###############################################

# Python program to
# demonstrate stack implementation
# using collections.deque
from collections import deque
 
stack = deque()
 
# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')
 
print('Initial stack:')
print(stack)
 
# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
 
print('\nStack after elements are popped:')
print(stack)