import time

class Node:
    def __init__(self, data):
        self.data = data  # Store node data
        self.next = None  # Pointer to next node


class LinkedList:
    def __init__(self):
        
        self.head = None  # Head initially null

# ADD DATA TO LIST
    def append(self, data):

        newNode = Node(data) # Create new Node

        if self.head is None: # If list empty
            self.head = newNode # Set new node as head
            return
        
        currentPos = self.head # If not empty start at head node
        while currentPos.next:#traverse through nodes
            currentPos = currentPos.next 
        currentPos.next = newNode # Set next pointer of the last node to new node

# DISPLAY DATA
    def display(self):

        currentPos = self.head # Start at the head of the list

        while currentPos: # Traverse list
            print(currentPos.data, end=" > ")
            currentPos = currentPos.next
        print ("Done") # End of list

def menu():

    myList = LinkedList()

    while True:
        time.sleep(1)
        selection = input("Select List Function:\n[1] Push\n[2] Pop\n[3] Reverse\n[4] Sort\n[5] Display\n>")

        if selection == '1':
            data = input("Enter data to push: ")
            time.sleep(1)
            #LinkedList.push(data)
            print("Pushed " + data + " to the list.")
            continue

        if selection == '2':
            LinkedList.pop()

        if selection == '3':
            LinkedList.reverse()

        if selection == '4':
            LinkedList.sort()

        if selection == '5':
            LinkedList.display()

        else:
            print("Please select an option from the list.")

print ("Linked List System")
menu()