import userinfo
import os
import userinfo 
import random
import ship
currentlocationif = "Earth"
number = int(0)
noitem = "You can't sell hopes and dreams!"
coalprice = 100
ironprice = 250 
diamondprice = 600
Flux_Capacitorprice = 1400
Spongebobprice = 1200

def sellmorefaster(item):
    global number
    os.system("clear")
    number = input("How much " + item  + " would you like to sell?\n\nChoose quantity:\n> ")
    if number.isdigit():
        number = int(number)
        if number <= 0:
            print("Sale Canceled")
        if number >= 1:
            return int(number)
    if not number.isdigit():
        while not number.isdigit():
            number = input("Invalid input. \nHow much " + item + " would you like to sell? \n >")
        number = int(number)
        return int(number)

def template():
    tryagain = "Placeholder"
    global currentlocationif
    global coalprice
    global ironprice
    global diamondprice
    global Flux_Capacitorprice
    global Spongebobprice
    
    if currentlocationif != ship.current_location_name:
        coalprice = int(random.uniform(0,500))
        ironprice = int(random.uniform(0, 750))
        diamondprice = int(random.uniform(0, 2600))
        Flux_Capacitorprice = int(random.uniform(0, 2600))
        Spongebobprice = int(random.uniform(0,2600))
        currentlocationif = ship.current_location_name
    userinfo.inventorygetforsell(coalprice,ironprice,diamondprice,Flux_Capacitorprice,Spongebobprice)
    option = input("\nChoose option:\n> ")

    if option == "1":
        if userinfo.Coal == 0:
            print(noitem)

        if userinfo.Coal > 0:
            sellmorefaster("Coal")
            if userinfo.Coal < number:
                while not tryagain == "n" and not tryagain == "N" and userinfo.Coal < number:
                    tryagain = input("You don't have that much to sell. Try again? (Y/N)\n\nChoose option:\n> ")
                    if tryagain == "y" or tryagain =="Y":
                        sellmorefaster("Coal")
            if userinfo.Coal >= number:
                userinfo.Coal -= number
                userinfo.units += (coalprice * number)
                print("You have sold " + str(number) + " Coal for " + str(coalprice * number) + ".")

    if option == "2":

        if userinfo.Iron == 0:
            print(noitem)

        if userinfo.Iron > 0:
            sellmorefaster("Iron")
            if userinfo.Iron < number:
                while not tryagain == "n" and not tryagain == "N" and userinfo.Iron < number:
                    tryagain = input("You don't have that much to sell. Try again? (Y/N)\n\nChoose option:\n> ")
                    if tryagain == "y" or tryagain == "Y":
                        sellmorefaster("Iron")
            if userinfo.Iron >= number:
                userinfo.Iron -= number
                userinfo.units += (ironprice * number)
                print("You have sold " + str(number) + " iron for " + str(ironprice * number) + ".")


    if option == "3":

        if userinfo.Diamond == 0:
            print(noitem)

        if userinfo.Diamond > 0:
            sellmorefaster("Diamond")
            if userinfo.Diamond < number:
                while not tryagain == "n" and not tryagain == "N" and userinfo.Diamond < number:
                    tryagain = input("You don't have that much to sell. Try again? (Y/N)\n\nChoose option:\n> ")
                    if tryagain == "y" or tryagain == "Y":
                        sellmorefaster("Diamond")
            if userinfo.Diamond >= number:
                userinfo.Diamond -= number
                userinfo.units += (diamondprice * number)
                print("You have sold " + str(number) + " diamond for " + str(ironprice * number) + ".")

    if option == "4":

        if userinfo.Flux_Capacitor == 0:
            print(noitem)

        if userinfo.Flux_Capacitor > 0:
            sellmorefaster("Flux Capacitor")
            if userinfo.Flux_Capacitor < number:
                while not tryagain == "n" and not tryagain == "N" and userinfo.Diamond < number:
                    tryagain = input("You don't have that much to sell. Try again? (Y/N)\n\nChoose option:\n> ")
                    if tryagain == "y" or tryagain == "Y" and userinfo.Flux_Capacitor < number:
                        sellmorefaster("Flux Capacitor")
            if userinfo.Flux_Capacitor >= number:  
                userinfo.Flux_Capacitor -= number
                userinfo.units += (Flux_Capacitorprice * number)
                print("You have sold " + str(number) + " Flux Capacitor for " + str(Flux_Capacitorprice * number) + ".")

    if option == "5":

        if userinfo.Spongebob == 0:
            print(noitem)

        if userinfo.Spongebob > 0:
            sellmorefaster("Spongebob")
            if userinfo.Spongebob < number:
                while not tryagain =="n" and not tryagain =="N" and userinfo.Spongebob:
                    tryagain = input("You don't have that much to sell. Try again? (Y/N)\n\nChoose option:\n> ")
                    if tryagain == "y" or tryagain == "Y" and userinfo.Spongebob < number:
                        sellmorefaster("Spongebob")
            if userinfo.Spongebob >= number:
                userinfo.Spongebob -= number
                userinfo.units += (Spongebobprice * number)
                print("You have sold " + str(number) + " Spongebob for " + str(Spongebobprice * number) + ".")

def earthsell(): 
    template(100,250,600,1400,1200)

def alphasell():
    template(150,250,900,800,1300)

def randomsell():
    template(200,400,1400,1600,800)
