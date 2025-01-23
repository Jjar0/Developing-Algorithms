import time  # Importing time for adding delays

# Class representing node in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # Store the value of the node
        self.next = None  # Pointer to the next node


# Class representing the linked list
class LinkedList:
    def __init__(self):
        self.head = None  # Initialise head of list as None (empty list)

    # DISPLAY DATA
    def display(self):
        # Check the list  empty
        if self.head is None:
            print("List is empty.")
            return

        # Traverse list from head and print each node
        currentPos = self.head  # Start at head of list
        while currentPos is not None:  # Continue until end of the list
            print(currentPos.data, end=" > " if currentPos.next else "\n")  # Format output
            currentPos = currentPos.next  # Move to next node

    # PUSH
    def push(self, data):
        # Create new node with given data
        newNode = Node(data)
        newNode.next = self.head  # Point new node to the current head
        self.head = newNode  # Update head

    # POP
    def pop(self):
        # Check if list empty
        if self.head is None:
            print("List is empty!")
            return None

        # Remove head node
        popData = self.head.data  # Get the data from head node
        self.head = self.head.next  # Update head to next node
        print(f"Popped: {popData}") 
        return popData

    # REVERSE
    def reverse(self):
        prevNode = None  # Initialise previous node as None
        currentPos = self.head

        # Iterate through list and reverse the links
        while currentPos is not None:
            nextNode = currentPos.next  # Store the next node
            currentPos.next = prevNode  # Reverse the link to point to the previous node
            prevNode = currentPos  # Move the previous pointer to the current node
            currentPos = nextNode  # Move to the next node
        self.head = prevNode  # Update the head to the new first node (previously last)
        print("Reversed the list.")

    # SORT
    def sort(self):
        # Check if list is empty or only has one element
        if self.head is None or self.head.next is None:
            print("List is too short to sort.")
            return

        # Extract data from linked list into a Python list
        dataList = []
        currentPos = self.head  # Start at head of list
        while currentPos is not None:
            dataList.append(int(currentPos.data))  # Convert data to int and add to list
            currentPos = currentPos.next  # Move to next node

        # Sort Python list
        dataList.sort()

        # Rebuild linked list with sorted data
        currentPos = self.head  # Start at head of list
        for data in dataList:
            currentPos.data = data  # Update node's data
            currentPos = currentPos.next  # Move to next node

        print("List has been sorted.")


# Menu
def menu():
    myList = LinkedList()  # Create a new linked list

    while True:
        time.sleep(1)
        selection = input(
            "Select List Function:\n[1] Push\n[2] Pop\n[3] Reverse\n[4] Sort\n[5] Display\n>"
        )
        # PUSH operation
        if selection == "1":
            data = input("Enter data to push: ")
            time.sleep(1) 
            try:
                intData = int(data)  # Validate input as an integer
                myList.push(intData)  # Push data to linked list
            except ValueError:
                print("You must enter an integer.")  # Handle invalid input
                continue

            print("Pushed " + data + " to the list.")
            myList.display()  # Display the updated list
            continue
        # POP operation
        elif selection == "2":
            myList.pop()  # Remove the first element from list
            myList.display()
            continue
        # REVERSE operation
        elif selection == "3":
            myList.reverse()  # Reverse order of the list
            myList.display() 
            continue
        # SORT operation
        elif selection == "4":
            myList.sort()  # Sort the list
            myList.display()
        # DISPLAY operation
        elif selection == "5":
            myList.display()  # Display the current state of the list
        # INVALID option
        else:
            print("Please select a valid option.")


# Start
if __name__ == "__main__": #check if main for testing 
    print("Linked List System")
    menu()