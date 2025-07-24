# Node class with constructor
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList class  
class LinkedList: 
    def __init__(self):
        self.head = None
    
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

        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

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