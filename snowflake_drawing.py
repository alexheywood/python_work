#Draw A Frieze Pattern

from turtle import *

#Draw Element 5 Times
for element in range (1, 6):

#Draw individual element
    for spokes in range (1, 9):

        forward(40)
        right(180)
        forward(40)
        right(45)
    penup()
    forward(100)
    pendown()
