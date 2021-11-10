from planets import earth
from planets import *
import math

far_away = [float(-10), float(-10)]
far_away1 = [float(10), float(10)]
starting_location = earth
current_location = starting_location
random_planet = random_location()
#destination = random_planet()

def distance():
    a = far_away[0] 
    b = far_away[1]
    c = far_away1[0]
    d = far_away1[1]
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
            s = a
            return s
        else:
            print('\nInvalid input\n')

def distance_convert():
    a = distance()
    a *= 20
    d = a
    d = round(d)
    return d

def time():
    d = distance_convert()
    s = warp_speed()
    t = d / s
    t = round(t, 3)
    return t

def fuel():
    s = warp_speed()
    a = distance()
    s /= 30
    f = s * a
    f = round(f, 3)
    return f

#print(distance())
#print(str('Fuel used: ')):w
#print(time())
#print(fuel())
#print(warp_speed())
