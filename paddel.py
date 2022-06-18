from turtle import Turtle



class Paddel(Turtle):
    def __init__(self, postion):
        super().__init__()
        paddel = Turtle()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(5, 1)
        self.goto(postion)

    
    def go_up(self):
         new_y = self.ycor() + 20
         self.goto(self.xcor(), new_y)

    def go_down(self):
         new_y = self.ycor() - 20
         self.goto(self.xcor(), new_y)
