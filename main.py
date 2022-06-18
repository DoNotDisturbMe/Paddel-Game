import time
from turtle import Turtle,  Screen
from paddel import Paddel
from ball import Ball
from scoreboard import Scoreboard
screen = Screen()
screen.bgcolor("black")
screen.title("Paddel Game")
screen.tracer(0)
screen.setup(height = 600,  width =  800)

r_paddel = Paddel((350, 0))
l_paddel = Paddel((-350, 0))
Balls = Ball()
Scoreboards = Scoreboard()





screen.listen()
screen.onkey(r_paddel.go_up, "Up")
screen.onkey(r_paddel.go_down, "Down")
screen.onkey(l_paddel.go_up, "w")
screen.onkey(l_paddel.go_down, "s")


game_is_one = True
while game_is_one:
    time.sleep(0.1)
    screen.update()
    Balls.move()


    #detect collision with wall
    if Balls.ycor() > 280 or Balls.ycor() <-280:
        Balls.bounce_y()

    #detect collision with paddel
    if Balls.distance(r_paddel) < 50 and Balls.xcor() >320  or Balls.distance(l_paddel) <50 and Balls.xcor() < -320:
        Balls.bounce_x()

    #detect R Paddle misses
    if Balls.xcor() > 380:
        Balls.reset_position()
        Scoreboards.l_point()

    #detect L Paddel misses
    if Balls.xcor() < -380:
        Balls.reset_position()
        Scoreboards.r_point()















screen.exitonclick()
