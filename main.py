from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?"
                                                          " Enter a color of the rainbow: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
y_position = -120
is_race_on = False

for color in colors:
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(color)
    tim.goto(x=-230, y=y_position)
    y_position += 50
    turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")


screen.exitonclick()


# etch-a-sketch code
# def move_forwards():
#     tim.forward(10)
#
#
# def move_backwards():
#     tim.backward(10)
#
#
# def rotate_counter_clockwise():
#     tim.left(10)
#
#
# def rotate_clockwise():
#     tim.right(10)
#
#
# def return_space():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
#
# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="a", fun=rotate_counter_clockwise)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="d", fun=rotate_clockwise)
# screen.onkey(key="c", fun=return_space)


