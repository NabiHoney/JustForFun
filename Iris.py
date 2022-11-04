from turtle import *
shape('circle')
speed(0)

def square(length=5):
    for i in range(3):
        forward(length)
        right(90)
        right(90)

def cir_square():
	for i in range(500):
		square(i*5+5)
		right (5)
		
cir_square()	
