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

print(starting_location)
print(destination)
print(distance())
