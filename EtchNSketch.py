"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle
import random
screen = turtle.Screen()
screen.title("Etch 'n Sketch Game")
t = turtle.Turtle()
pen_size = 1

# Function to move the turtle
def move_up():
    t.setheading(90)
    t.forward(10)

def move_down():
    t.setheading(270)
    t.forward(10)

def move_left():
    t.setheading(180)
    t.forward(10)

def move_right():
    t.setheading(0)
    t.forward(10)

# Function to lift the pen
def pen_up():
    t.penup()

# Function to put the pen down
def pen_down():
    t.pendown()

# Function to erase the screen
def erase():
    t.clear()
# Function to change the color 
def changeColor():
  t.pencolor(random.random(),random.random(),random.random())

# Function to make pen bigger
def pen_bigger():
    global pen_size
    pen_size += 1
    t.pensize(pen_size)

# Function to make pen smaller
def pen_smaller():
    global pen_size
    if pen_size > 1:
        pen_size -= 1
    t.pensize(pen_size)


# Keyboard bindings
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(pen_up, "u")
screen.onkey(pen_down, "d")
screen.onkey(changeColor,"c")
screen.onkey(pen_bigger, "b")
screen.onkey(pen_smaller, "s")
screen.onkey(erase, "space")



print("Welcome to Etch 'N Sketch Game!")
print("Use the key board arrows to move around the turtle sprite!!!")
print("(u)-pen up (d)-pen down (c)-change color ")
print("(b)-make pen bigger (s)-make pen smaller (space bar)-erase screen")
