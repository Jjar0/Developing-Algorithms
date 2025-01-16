import turtle

class KochSnowflake:
    def __init__(self, depth, sideLength):

        self.depth = depth
        self.sideLength = sideLength
        self.t = turtle.Turtle()
        self.screen = turtle.Screen()

    def config(self):

        self.screen.bgcolor("white")
        self.t.speed(0)
        self.t.penup()
        self.t.goto(-self.sideLength / 2, self.sideLength / 3)  # Adjust starting position
        self.t.pendown()
        self.t.hideturtle()

    def drawSegment(self, length, depth):

        if depth == 0:
            self.t.forward(length)
        else:
            length /= 3.0
            self.drawSegment(length, depth - 1)
            self.t.left(60)
            self.drawSegment(length, depth - 1)
            self.t.right(120)
            self.drawSegment(length, depth - 1)
            self.t.left(60)
            self.drawSegment(length, depth - 1)

    def drawSnowflake(self):
  
        for _ in range(3):  # Three sides of the snowflake
            self.drawSegment(self.side_length, self.depth)
            self.t.right(120)

    def run(self):

        self.config()
        self.drawSnowflake()
        self.screen.mainloop()


snowflake = KochSnowflake(depth=4, side_length=400)
snowflake.run()


