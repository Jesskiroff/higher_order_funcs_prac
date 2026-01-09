from turtle import Turtle, Screen



screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

tim = Turtle
tim.shape("turtle")
tim.color("red")


# def forward():
#     tim.forward(10)

# def backward():
#     tim.backward(10)

# def left():
#     tim.left(10)

# def right():
#     tim.right(10)


# def reset():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()

# screen.listen()
# screen.onkey(forward, "f")
# screen.onkey(backward, "b")
# screen.onkey(left, "l")
# screen.onkey(right, "r")
# screen.onkey(reset, "c")
screen.exitonclick()