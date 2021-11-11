from planets import *
import math
import os

# define variables

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
available_areas = [available_areas_names, available_areas_locations]
#destination = alpha_location

# define functions

#def current_location():
#    current_location = destination

def distance(destination):
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
    a = str(a)
    return a

def warp_speed():
    a = ()
    while a == ():
        os.system("clear")
        print('\nPlease calculate how fast you would like to travel')
        W = input('\nInput integer 1-8 (higher number = faster travel and fuel consumed at higher rate)\n> ')
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

def distance_convert(distance):
    distance = float(distance)
    a = distance
    a *= 20
    d = a
    d = round(d)
#    d = str(d)
    d = float(d)
    return d
    if 'd' in locals():
        del d

def time(speed, dist_con):
    d = dist_con
    s = speed
    t = d / s
    t = round(t, 3)
    return t

def fuel(speed, distance):
    s = speed
    distance = float(distance)
    a = distance
    s /= 30
    f = s * a
    f = round(f, 3)
    return f

def travel_ui():
    global current_location
    global distance
    global current_location_name
    global available_areas_locations
    os.system("clear")
    k = 0
    global current_fuel
    available_areas_names.remove(current_location_name)
    available_areas_locations.remove(current_location)
    current_fuel = str(current_fuel)
    while k == 0:
        l = 0
        while l == 0:
            n = 0
            os.system("clear")
            print('Travel Menu\n')
            print(str('Current location: ') + (current_location_name))
            print(str('Current fuel level: ') + (current_fuel) + str(' gal\n'))
            print('Planets available to travel to: ')
            for i in available_areas_names:
                n += 1
                print(str(n) + '. ' + i)
            destination = str(input('\nSelect number of planet to travel to or (E)xit Travel Menu:\n> '))
            destination = str(destination)
            if destination == 'e' or destination == 'E':
                k = 1
                l = 1
            elif destination == '1' or destination == '2':
                destination = int(destination)
                destination = available_areas_names[int(destination) -1]
                if destination == available_areas_names[0]:
                    os.system("clear")
                    print('\nYou have selected ' + destination + '...\n')
                    if 'destination' in locals():
                        del destination
                    destination = available_areas_locations[0]
                    distance = (distance(destination))
                    print('This is ', distance, ' units away.')
                    speed = warp_speed()
                    dist_con = distance_convert(distance)
                    time_used = time(speed,dist_con)
                    fuel_used = fuel(speed,distance)
                    print('\nYears to travel: ', time_used, 'years', '\nFuel to be used: ', fuel_used, 'gal')
                    travel = input('\nDo you want to travel? (Y)es, (N)o\n> ')
                    if travel == 'y' or travel == 'Y':
                        current_fuel = float(current_fuel)
                        fuel_used = float(fuel_used)
                        destination = available_areas_names[0]
                        current_fuel -= fuel_used
                        current_location_name = destination
                        current_location = available_areas_locations[0]
                        return current_fuel, current_location_name
                        l += 1
                    else:
                        l = 1
                if destination == available_areas_names[1]:
                    os.system("clear")
                    print('\nYou have selected ' + destination + '...\n')
                    destination = available_areas_locations[1]
                    distance = distance(destination)
                    print('This is ', distance, ' units away.')
                    speed = warp_speed()
                    dist_con = distance_convert(distance)
                    time_used = time(speed,dist_con)
                    fuel_used = fuel(speed,distance)
                    print('\nYears to travel: ', time_used, 'years', '\nFuel to be used: ', fuel_used, 'gal')
                    travel = input('\nDo you want to travel? (Y)es, (N)o\n> ')
                    if travel == 'y' or travel == 'Y':
                        current_fuel = float(current_fuel)
                        current_fuel = round(current_fuel, 3)
                        fuel_used = float(fuel_used)
                        destination = available_areas_names[1]
                        current_fuel -= fuel_used
                        current_location_name = destination
                        current_location = available_locations_areas[1]
                        return current_fuel, current_location_name
                        l += 1
                    else:
                        l = 1
            else:
                print('Invalid input')
                l = 0
        
#print(distance())
#print(time())
#print(fuel())
#print(warp_speed())
#print(earth_info)
print(travel_ui())
