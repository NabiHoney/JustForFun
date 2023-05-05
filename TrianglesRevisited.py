"Triangles Revisited"
from turtle import *
shape('turtle')
speed(0)
def triangle(sidelength = 100):
    for i in range(3):
        forward(sidelength)
        right(120) #uses external NOT internal ang.
        
def repeater():
    for i in range(75):
        triangle()
        left (35)

def mover():
    for i in range(25):
        repeater()
        forward(100)

mover()
