from turtle import *


#we want to paint a house

#step 1: draw a square
shape("turtle")
width(6)
speed(0)
color("blue")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)


forward(70)
color("red")
begin_fill()
left(90)
forward(120)  
right(90)
forward(60)
right(90)
forward(120)
right(90)
forward(60)
end_fill()

penup()
goto(200,200)
pendown()

color("green")
begin_fill()
right(60)
forward(200)
left(120)
forward(200)
end_fill()

exitonclick()