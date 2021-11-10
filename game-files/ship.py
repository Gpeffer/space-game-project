from planets import *
import math

earth_name = str('Earth')
random_planet_name = str('Random Planet')
alpha_name = str('Alpha Aproxima')

earth_info = [earth_name, earth_location]
alpha_info = [alpha_name, alpha_location]
random_planet_info = [random_planet_name, random_planet_location]

starting_location_name = earth_name
starting_location = earth_location
current_location_name = starting_location_name
current_location = earth_location #starting_location

starting_fuel = 100.0
current_fuel = starting_fuel
available_areas_names = ["Earth", "Alpha Aproxima", "Random Planet"]
available_areas_locations = [earth_location, alpha_location, random_planet_location]
destination = alpha_location

def travel_ui():
    n = 0
    global current_fuel
    available_areas_names.remove(current_location_name)
    available_areas_locations.remove(current_location)
    current_fuel = str(current_fuel)
    print('Travel Menu\n')
    print(str('Current location: ') + (current_location_name))
    print(str('Current fuel level: ') + (current_fuel) + str(' gal\n'))
    print('Planets available to travel to: ')
    for i in available_areas_names:
        n += 1
        print(str(n) + '. ' + i + ' ')
    destination = input('\nSelect number of planet to travel to:\n> ')
    destination = available_areas_names[int(destination) -1]
    return destination

#def current_location():
#    current_location = destination

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
#print(time())
#print(fuel())
#print(warp_speed())
#print(earth_info)
print(travel_ui())
