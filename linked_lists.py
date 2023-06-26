class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    def append(self, new_node):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def print(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

e1 = Node(1)
e2 = Node(2)

ll = LinkedList(e1)
ll.append(e2)
ll.print()