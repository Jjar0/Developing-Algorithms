import turtle

class KochSnowflake:
    def __init__(self, depth, sideLength):
        # Initialize the KochSnowflake with recursion depth and side length
        self.depth = depth
        self.sideLength = sideLength
        self.t = turtle.Turtle()  # Create turtle object
        self.screen = turtle.Screen()  # Create screen object for drawing

    def config(self):
        # Configure the screen and turtle
        self.screen.bgcolor("white")
        self.t.speed(0)  # Set turtle's speed to the maximum
        self.t.penup() 
        # Move the turtle to the starting position for centring the snowflake
        self.t.goto(-self.sideLength / 2, self.sideLength / 3)
        self.t.pendown()
        self.t.hideturtle()

    def drawSegment(self, length, depth):
        # Recursively draw one segment of the Koch curve
        if depth == 0:
            # BASE CASE: if depth 0 draw a straight line
            self.t.forward(length)
        else:
            # RECUSRIVE CASE: divide segment into thirds
            length /= 3.0
            # Draw the first segment
            self.drawSegment(length, depth - 1) 
            self.t.left(60)
            # Draw the second segment
            self.drawSegment(length, depth - 1)
            self.t.right(120)
            # Draw third segment
            self.drawSegment(length, depth - 1)
            self.t.left(60)
            # Draw fourth segment
            self.drawSegment(length, depth - 1)

    def drawSnowflake(self): # Draw Koch snowflake
        for _ in range(3):  # Loop to draw three sides of triangle
            self.drawSegment(self.sideLength, self.depth)  # Draw one side
            self.t.right(120)  # Turn right 120 degrees to start next side

    def run(self):
        # Main to configure turtle and draw snowflake
        self.config()  # Set up drawing
        self.drawSnowflake()  # Draw Koch snowflake
        self.screen.mainloop()  # Keep screen open

# Create KochSnowflake class instance with specified depth and side length
snowflake = KochSnowflake(depth=4, sideLength=400)
snowflake.run()