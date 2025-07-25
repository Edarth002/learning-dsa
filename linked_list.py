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


    def append(self, data):
        newNode = Node(data)

        if not self.head:
            self.head = newNode
            return
        lastNode = self.head

        while lastNode.next:
            lastNode = lastNode.next

        lastNode.next = newNode

# Case 2: Insert operation which takes constant time, only that the time taken to find the actual 
# target index(position etc) takes linear time

    def insert(self, data, key):
        current = self.head
        prev = None
        while current.data != key:
            prev = current
            current = current.next
        newNode = Node(data)
        prev.next = newNode
        current.

        

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


# Operations performed on Linked Lists

# Searching
    def search(self, key):
        current = self.head

        while current:
            if current.data == key:
                print(key, end=" Is found in the list")
                return      
            current = current.next
        
        print(key, end=" Not found in the list")



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
        prev = None
        while current.data != key:
            prev = current
            current = current.next
        
        if current is None:
            print("Value not found in the list")
        else:
            prev.next = current.next
            current = None
            print(key, end=" Has been deleted")

# Example Usage
myList = LinkedList()
myList.append(10)
myList.append(20)
myList.append(30)
myList.append(40)
myList.append(50)

print("My LinkedList values are given as: ")
myList.display()

myList.prepend(15)
print("My LinkedList after prepending 15")
myList.display()

myList.append(100)
print("My LinkedList after appending 100")
myList.display()

myList.delete(30)
print("My LinkedList after deleting 30")
myList.display()

myList.search(12)