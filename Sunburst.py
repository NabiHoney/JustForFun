from turtle import *
shape('classic')
speed(0)

def square():
    for i in range(72):
        right(5)
        forward(100)
        right(90)
square()
right(45)
forward(19)

def center_square():
    for i in range(36):
        right(5)
        forward(100)
        right(90)
        right(90)
center_square()
