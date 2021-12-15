# importing modules

from planets import *
import math
import userinfo
import os
import stdrandom
import userinfo

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
destruct = int(0)

# define functions

def distance1(destination):
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
        print('\nPlease calculate how fast you would like to travel')
        W = input('\nInput integer 1-8 (higher number = faster travel and fuel consumed at higher rate)\n> ')
        if W == '1' or W == '2' or W == '3' or W == '4' or W == '5' or W == '6' or W == '7' or W == '8':
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
            os.system("clear")
            print('\nInvalid input')

def distance_convert(distance):
    distance = float(distance)
    a = distance
    a *= 20
    d = a
    d = round(d)
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
    global units
    global earthitems
    global current_location
    global distance
    global current_location_name
    global available_areas_locations
    global available_areas_names
    global available_areas
    global destruct
    os.system("clear")
    k = 0
    global current_fuel
    for i in available_areas_names:
        if(i == current_location_name) :
            available_areas_names.remove(current_location_name)
    for i in available_areas_locations:
        if(i == current_location) :
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
                    distance = distance1(destination)
                    print('This is', distance, 'units away.')
                    speed = warp_speed()
                    dist_con = distance_convert(distance)
                    time_used = time(speed,dist_con)
                    fuel_used = fuel(speed,distance)
                    print('\nYears to travel: ', time_used, 'years', '\nFuel to be used: ', fuel_used, 'gal')
                    travel = input('\nDo you want to travel? (Y)es, (N)o\n> ')
                    if travel == 'y' or travel == 'Y':
                        os.system("clear")
                        current_fuel = float(current_fuel)
                        fuel_used = float(fuel_used)
                        destination = available_areas_names[0]
                        current_fuel -= fuel_used
                        time_used = round(time_used, 1)
                        userinfo.player.age += time_used
                        current_location_name = destination
                        current_location = available_areas_locations[0]
                        available_areas_names = ["Earth", "Alpha Aproxima", "Random Planet"]
                        available_areas_locations = [earth_location, alpha_location, random_planet_location]
                        available_areas = [available_areas_names, available_areas_locations]
                        if 'v' in locals():
                            del v
                        v = stdrandom.uniformInt(1,10)
                        u = 0
                        while u == 0:
                            os.system("clear")
                            if v == 1:
                                print('\nCongratulations! You found a meteorite containing Coal!')
                                print('\nItem will automatically be added to your inventory.')
                                userinfo.player.Coal += 1
                                v = input('\nPress enter to continue to your destination.\n> ')
                            elif v == 2:
                                print('\nCongratulations! You found a meteorite containing Iron!')
                                print('\nItem will automatically be added to your inventory.')
                                userinfo.player.Iron += 1
                                v = input('\nPress enter to continue to your destination.\n> ')
                            elif v == 3:
                                print('\nCongratulations! You found a meteorite containing Diamonds!')
                                print('\nItem will automatically be added to your inventory.')
                                userinfo.player.Diamond += 1
                                v = input('\nPress enter to continue to your destination.\n> ')
                            elif v == 4:
                                print('\nCongratulations! You found a meteorite containing a Flux Capacitor!')
                                print('\nItem will automatically be added to your inventory.')
                                userinfo.player.Flux_Capacitor += 1
                                v = input('\nPress enter to continue to your destination.\n> ')
                            elif v == 5:
                                print('\nCongratulations! You found a meteorite containing SPONGEBOB!')
                                print('\nItem will automatically be added to your inventory.')
                                userinfo.player.Spongebob += 1
                                v = input('\nPress enter to continue to your destination.\n> ') 
                            u += 1
                        current_fuel = round(current_fuel)
                        if current_fuel < 0.0:
                            os.system("clear")
                            print('Oh no! You\'ve ran out of fuel while traveling among the stars.')
                            input('\nPress enter to continue.\n> ')
                            os.system("clear")
                            print('The Galaxy is a dangerous place to be floating around aimlessly.\nYou\'ve become a target.')
                            input('\nPress enter to continue.\n> ')
                            os.system("clear")
                            print('Some space Pirates spot you from their vessel and take interest.\nYou had better act quick. What will you do?\n')
                            pirates = ['Try to find extra fuel stored on ship (Take chance to find enough fuel to complete journey)', 'Hit self-destruct button (Don\'t give them the pleasure)', 'Try to bribe the Pirates 1000 units to leave you alone']
                            num = 0
                            for i in pirates:
                                num += 1
                                num = str(num)
                                print(num + '.', i)
                                num = int(num)
                            choice = input('\nChoose option:\n> ')
                            loop = 0
                            while loop == 0:
                                if choice == '1':
                                    os.system("clear")
                                    randint = stdrandom.uniformInt(1,2)
                                    input('Searching...\n\nPress enter to continue.\n> ')
                                    os.system("clear")
                                    if randint == '1':
                                        print('Yes! You found just enough spare fuel you had stowed away for a rainy day.\nYou fuel up as quick as possible and continue to your destination.')
                                        input('\nPress enter to arrive at your destination (make sure to get some fuel)\n> ')
                                        current_fuel = 0
                                    else:
                                        print('Oh no! There\'s no spare fuel to be found. There Pirates make short work of you. You\'re dead.')
                                        input('\nPress enter to continue.\n> ')
                                        destruct += 1
                                    if randint in locals():
                                        del randint
                                    loop += 1
                                elif choice == '2':
                                    os.system("clear")
                                    print('BOOM')
                                    input('\nPress enter to continue.\n> ')
                                    destruct += 1
                                    loop += 1
                                elif choice == '3':
                                    os.system("clear")
                                    print('You try pay the Pirates 1000 units to leave you alone...')
                                    input('\nPress enter to continue.\n> ')
                                    os.system("clear")
                                    randunit = userinfo.player.units - 1000
                                    if randunit < 0:
                                        print('You don\'t have enough units to pay the pirates. You\'re dead.')
                                        input('\nPress enter to continue.\n> ')
                                        destruct += 1
                                    else:
                                        print('You pay the pirates off successfully,\nand manage to extract enough fuel from nearby asteroids to complete your journey.')
                                        input('\nPress enter to continue to your destination.\n> ')
                                        userinfo.player.units -= 1000
                                        current_fuel = 0
                                    if randunit in locals():
                                        del randunit
                                    loop += 1
                                else:
                                    choice = input('\nInvalid input. Please try again.\n> ')
                        return current_fuel, current_location_name, destruct, userinfo.player.units
                        l += 1
                    else:
                        l = 1
                if destination == available_areas_names[1]:
                    os.system("clear")
                    print('\nYou have selected ' + destination + '...\n')
                    destination = available_areas_locations[1]
                    distance = distance1(destination)
                    print('This is', distance, 'units away.')
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
                        time_used = round(time_used, 1)
                        userinfo.player.age += time_used
                        current_location_name = destination
                        current_location = available_areas_locations[1]
                        available_areas_names = ["Earth", "Alpha Aproxima", "Random Planet"]
                        available_areas_locations = [earth_location, alpha_location, random_planet_location]
                        available_areas = [available_areas_names, available_areas_locations]
                        if 'v' in locals():
                            del v
                        v = stdrandom.uniformInt(1,10)
                        u = 0
                        while u == 0:
                            os.system("clear")
                            if v == 1:
                                print('\nCongratulations! You found a meteorite containing Coal!')
                                print('\nItem will automatically be added to your inventory.')
                                userinfo.player.Coal += 1
                                v = input('\nPress enter to continue to your destination.\n> ')
                            elif v == 2:
                                print('\nCongratulations! You found a meteorite containing Iron!')
                                print('\nItem will automatically be added to your inventory.')
                                userinfo.player.Iron += 1
                                v = input('\nPress enter to continue to your destination.\n> ')
                            elif v == 3:
                                print('\nCongratulations! You found a meteorite containing Diamonds!')
                                print('\nItem will automatically be added to your inventory.')
                                userinfo.player.Diamond += 1
                                v = input('\nPress enter to continue to your destination.\n> ')
                            elif v == 4:
                                print('\nCongratulations! You found a meteorite containing a Flux Capacitor!')
                                print('\nItem will automatically be added to your inventory.')
                                userinfo.player.Flux_Capacitor += 1
                                v = input('\nPress enter to continue to your destination.\n> ')
                            elif v == 5:
                                print('\nCongratulations! You found a meteorite containing SPONGEBOB!')
                                print('\nItem will automatically be added to your inventory.')
                                userinfo.player.Spongebob += 1
                                v = input('\nPress enter to continue to your destination.\n> ')
                            u += 1
                        current_fuel = round(current_fuel)
                        if current_fuel < 0.0:
                            os.system("clear")
                            print('Oh no! You\'ve ran out of fuel while traveling among the stars.')
                            input('\nPress enter to continue.\n> ')
                            os.system("clear")
                            print('The Galaxy is a dangerous place to be floating around aimlessly.\nYou\'ve become a target.')
                            input('\nPress enter to continue.\n> ')
                            os.system("clear")
                            print('Some space Pirates spot you from their vessel and take interest.\nYou had better act quick. What will you do?\n')
                            pirates = ['Try to find extra fuel stored on ship (Take chance to find enough fuel to complete journey)', 'Hit self-destruct button (Don\'t give them the pleasure)', 'Try to bribe the Pirates 1000 units to leave you alone']
                            num = 0
                            for i in pirates:
                                num += 1
                                num = str(num)
                                print(num + '.', i)
                                num = int(num)
                            choice = input('\nChoose option:\n> ')
                            loop = 0
                            while loop == 0:
                                if choice == '1':
                                    os.system("clear")
                                    randint = stdrandom.uniformInt(1,2)
                                    input('Searching...\n\nPress enter to continue.\n> ')
                                    os.system("clear")
                                    if randint == '1':
                                        print('Yes! You found just enough spare fuel you had stowed away for a rainy day.\nYou fuel up as quick as possible and continue to your destination.')
                                        input('\nPress enter to arrive at your destination (make sure to get some fuel)\n> ')
                                        current_fuel = 0
                                    else:
                                        print('Oh no! There\'s no spare fuel to be found. There Pirates make short work of you. You\'re dead.')
                                        input('\nPress enter to continue.\n> ')
                                        destruct += 1
                                    if randint in locals():
                                        del randint
                                    loop += 1
                                elif choice == '2':
                                    os.system("clear")
                                    print('BOOM')
                                    input('\nPress enter to continue.\n> ')
                                    destruct += 1
                                    loop += 1
                                elif choice == '3':
                                    os.system("clear")
                                    print('You try pay the Pirates 1000 units to leave you alone...')
                                    input('\nPress enter to continue.\n> ')
                                    os.system("clear")
                                    randunit = userinfo.player.units - 1000
                                    if randunit < 0:
                                        print('You don\'t have enough units to pay the pirates. You\'re dead.')
                                        input('\nPress enter to continue.\n> ')
                                        destruct += 1
                                    else:
                                        print('You pay the pirates off successfully,\nand manage to extract enough fuel from nearby asteroids to complete your journey.')
                                        input('\nPress enter to continue to your destination.\n> ')
                                        userinfo.player.units -= 1000
                                        current_fuel = 0
                                    if randunit in locals():
                                        del randunit
                                    loop += 1
                                else:
                                    choice = input('\nInvalid input. Please try again.\n> ')
                        return current_fuel, current_location_name
                        l += 1
                    else:
                        l = 1
            else:
                print('Invalid input')
                l = 0
