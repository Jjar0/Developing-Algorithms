import turtle

def draw(branchLength, t):
    if branchLength > 5:  # To stop recursion
# Main branch
        t.forward(branchLength)

# Draw right subtree
        t.right(20)  # Turn 20 degrees right
        draw(branchLength - 15, t)  # Recursive call for right subtree

# Return to Main
        t.left(40)  # Turn the turtle 40 degrees left
        draw(branchLength - 15, t)  # Recursive call for left subtree

# Return to the original angle
        t.right(20)
        t.backward(branchLength)

# Turtle config
def main():
    view = turtle.Screen()
    view.bgcolor("white")

    t = turtle.Turtle()
    t.shape("turtle")
    t.speed(5)  # Set fast speed

    t.left(90)  # Point up
    t.penup()
    t.goto(0, -250)  # Start at the bottom of the screen
    t.pendown()

    draw(100, t) #Draw

    view.mainloop()

main()

