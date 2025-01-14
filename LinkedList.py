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

        currentPos = self.head # Start at the head of the list

        while currentPos: # Traverse list
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

            prev = None
            currentPos = self.head
            while currentPos:
                nextNode = currentPos.next
                currentPos.next = prev
                prevNode = currentPos
                currentPos = nextNode
            self.head = prevNode
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
            continue

        if selection == '2':
            myList.pop()
            continue

        if selection == '3':
            myList.reverse()
            continue

        if selection == '4':
            myList.sort()

        if selection == '5':
            myList.display()

        else:
            print("Please select an option from the list.")

print ("Linked List System")
menu()