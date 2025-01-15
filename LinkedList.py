import time

class Node:
    def __init__(self, data):
        self.data = data  # Store node data
        self.next = None  # Pointer to next node


class LinkedList:
    def __init__(self):
        
        self.head = None  # Head initially null

# DISPLAY DATA
    def display(self):

        currentPos = self.head # Start at head of the list

        while currentPos is not None: # Traverse list
            print(currentPos.data, end=" > ")
            currentPos = currentPos.next
        print ("Done") # End of list

# PUSH 
    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

# POP
    def pop(self):

            if self.head is None: #Empty List validation
                print("List is empty!")
                return None

            popData = self.head.data
            self.head = self.head.next #Shifts data over one position
            print("Popped: " + popData)
            return popData
# REVERSE
    def reverse(self):

            prevNode = None
            currentPos = self.head # Start at the head of list

            while currentPos is not None:
                nextNode = currentPos.next # Store the next node
                currentPos.next = prevNode # Reverse the link
                prevNode = currentPos # Move previous pointer to current node
                currentPos = nextNode # Move to next node
            self.head = prevNode # Update the head to the last node
            print("Reversed List.")


def menu():

    myList = LinkedList()

    while True:
        time.sleep(1)
        selection = input("Select List Function:\n[1] Push\n[2] Pop\n[3] Reverse\n[4] Sort\n[5] Display\n>")

        if selection == '1':
            data = input("Enter data to push: ")
            time.sleep(1)
            myList.push(data)
            print("Pushed " + data + " to the list.")
            myList.display()
            continue

        if selection == '2':
            myList.pop()
            myList.display()
            continue

        if selection == '3':
            myList.reverse()
            myList.display()
            continue

        if selection == '4':
            myList.sort()
            myList.display()

        if selection == '5':
            myList.display()

        else:
            print("Please select an option from the list.")

print ("Linked List System")
menu()