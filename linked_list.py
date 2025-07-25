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
        count = 0
        while current:
            count += 1
           
            print(current.data, end=" -> ")
            current = current.next
        print("None")
        print(count, end=" is the size of linkedlist")
# Case 2: Insert operation which takes constant time, only that the time taken to find the actual 
# target index(position etc) takes linear time

    def insert(self, data, position):
        newNode = Node(data)
    # If list is empty
        if self.head == None:
            print("This data structure is empty, try creating one before Inserting data,"
            " or create one with this node as the head")
            return
    # If position is invalid, eg negative number or 0
        if position < 1:
            print("Invalid position in the linkedlist")
            return
    # If position is head
        if position == 1:
            self.next = self.head
            self.head = newNode
            return 
    # Traverse list to find target position 
        current = self.head
        prev = None
        count = 1
        while count < position:
            if current:
                prev = current
                current = current.next
            count = count + 1
        if current == None:
            print("Position does not exist in the list")
            return
        newNode.next = current
        prev.next = newNode




# Example Usage
myList = LinkedList()
myList.apppend(10)
myList.apppend(30)
myList.apppend(50)

# print("My LinkedList values are given as: ")
# myList.display()

# myList.apppend(100)
# print("My LinkedList after appending 100")
# myList.display()

myList.insert(70, 1)
print("My LinkedList after inserting 70 at postion 3")
myList.display()

