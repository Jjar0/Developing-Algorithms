class Node:
    def __init__(self, data):
        self.data = data  # Store node data
        self.next = None  # Pointer to next node


class LinkedList:
    def __init__(self):
        
        self.head = None  # Head initially null

    def append(self, data):

        newNode = Node(data) # Create new Node

        if self.head is None: # If list empty
            self.head = newNode # Set new node as head
            return
        
        currentPos = self.head # If not empty start at head node
        while currentPos.next:#traverse through nodes
            currentPos = currentPos.next 
        currentPos.next = newNode # Set next pointer of the last node to new node

    def display(self):

        currentPos = self.head # Start at the head of the list

        while currentPos: # Traverse list
            print(currentPos.data, end=" > ")
            currentPos = currentPos.next
        print ("Done") # End of list

myList = LinkedList()

myList.append(1)
myList.append(2)
myList.append(3)

myList.display()