from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]



for turtle_index in range(0, len(colors)):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.goto(x=-230, y=y_positions[turtle_index])
    tim.color(colors[turtle_index])
    

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