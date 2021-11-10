from planets import earth
from planets import *
import math

starting_location = earth
current_location = starting_location
random_planet = random_location()
destination = random_planet

def distance():
    a = current_location[0]
    b = current_location[1]
    c = destination[0]
    d = destination[1]
    a -= c
    b -= d
    a = a**2
    b = b**2
    a += b
    a = math.sqrt(a)
    a = round(a, 3)
    return a

def warp_speed():
    a = ()
    while a == ():
        W = input('Input integer 1-8 (higher number = faster travel and fuel consumed at higher rate)\n> ')
        W = int(W)
        if W <= 8 and W >= 1:
            W = float(W)
            a = float(10) / float(3)
            a = W**a
            b = float(-11) / float(3)
            c = float(10) - W
            b = c**b
            a += b
            a = round(a)
            return a
        else:
            print('\nInvalid input\n')

print(warp_speed())
