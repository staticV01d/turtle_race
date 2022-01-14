import random
from turtle import Turtle, Screen

# create screen and set size
screen = Screen()
screen.setup(width=500, height=400)

# list of colors
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

# create six turtles
tim = Turtle(shape="turtle")
tom = Turtle(shape="turtle")
don = Turtle(shape="turtle")
mic = Turtle(shape='turtle')
leo = Turtle(shape='turtle')
raph = Turtle(shape='turtle')
print(tim.shapesize())
# put turtles into a list
turtles = list([tim, tom, don, mic, leo, raph])

# Draw finish line with referee turtle
ref_turtle = Turtle(shape='triangle')
ref_turtle.penup()
ref_turtle.goto(230, 230)
ref_turtle.right(90)
ref_turtle.pendown()
while ref_turtle.ycor() > -230:
    ref_turtle.forward(10)
ref_turtle.hideturtle()

# take user bet
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)

# move turtles to starting position
i = 0
dist = 50

for t in turtles:
    t.penup()
    t.fillcolor(colors[i])
    i += 1
    t.goto(-230, -165 + (dist * i))

is_racing = False

# start race if user has entered bet
if user_bet:
    is_racing = True

# run the race
while is_racing:
    for t in turtles:
        if t.xcor() > 230:  # check if winner
            is_racing = False
            winning_color = t.fillcolor()
            if winning_color == user_bet:
                print("You've won! The {} turtle is the winner!".format(t.fillcolor()))
            else:
                print("You've lost! The {} turtle is the winner!".format(winning_color))
        # if not winner, move forward by random distance
        distance = random.randint(0, 10)
        t.forward(distance)


# EXIT
screen.exitonclick()
