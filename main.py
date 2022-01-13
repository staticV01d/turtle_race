from turtle import Turtle, Screen

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

tim = Turtle(shape="turtle")
tom = Turtle(shape="turtle")
don = Turtle(shape="turtle")
mic = Turtle(shape='turtle')
leo = Turtle(shape='turtle')
raph = Turtle(shape='turtle')

turtles = [tim, tom, don, mic, leo, raph]


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
for c in colors:
    for t in turtles:
        t.penup()
        t.fillcolor(c)
        t.goto(-230, -100)


#
screen.exitonclick()
