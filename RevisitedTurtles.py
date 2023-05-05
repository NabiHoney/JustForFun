"""Revisited Turtle"""

from turtle import *
speed(0)
def square():
    for i in range(100):
        forward(100)
        right(90)
        left(35)

def smol_square():
    for i in range(100):
        forward(50)
        right(90)
        left(35)

def smoller_square():
    for i in range(60):
        forward(10)
        right(90)
        left(35)

def repeater():
    for i in range(20):
        square()
        smol_square()
        smoller_square()

repeater()
