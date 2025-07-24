# Node class with constructor
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList class  
class LinkedList: 
    def __init__(self):
        self.head = None

# Insertion
# Case1: Tecnically not really insert since it uses prepend and append, adds
# data to the head or tail of the list
    def prepend(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode


    def apppend(self, data):
        newNode = Node(data)

        if not self.head:
            self.head = newNode
            return
        lastNode = self.head

        while lastNode.next:
            lastNode = lastNode.next

        lastNode.next = newNode

#Display function
    def display(self):
        current = self.head
        count = 0

        while current:
            count += 1
            
            print(current.data, end=" -> ")
            current = current.next
        print("None")
        print("Size of the Linked List is: ", count)
# Example Usage
myList = LinkedList()
myList.apppend(10)
myList.apppend(30)
myList.apppend(50)

print("My LinkedList values are given as: ")
myList.display()

myList.apppend(100)
print("My LinkedList after appending 100")
myList.display()

# Operations performed on Linked Lists

# Accessing, Searching


# Deletion 
def delete(self, key):
    current = self.head

    # Case 1: if the head node holds that data to be deleted, 
    # in most cases, this function is irrelevant if Case 2 is present

    if current.data == key:
        self.head = current.next
        current.data = None

   # Case 2: Traverses the whole list to delete the target data, 
   # O(n) and therefore arrays perform better here