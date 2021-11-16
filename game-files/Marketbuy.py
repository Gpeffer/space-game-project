import userinfo
import ship
import os

items = "nothing"
onetimeprint = 0
number = 1

def buymorethanone(item):
    global number
    os.system("clear")
    number = input("How much " + item  + " would you like to buy?\n\nChoose quantity:\n> ")
    if number.isdigit():
        number = int(number)
        if number <= 0:
            print("Purchase Canceled")
        if number >= 1:
            return int(number)
    if not number.isdigit():
        while not number.isdigit():
            os.system("clear")
            number = input("Invalid input. \nHow much " + item + " would you like to buy?\n\nChoose quantity:\n> ")
        number = int(number)
        return int(number)


def buytemp(UniqItem, CoalPrice, IronPrice, UniqItemPrice):
    global onetimeprint
    global number
    global items
    global units
    tryagain = "Placeholder"
    print("Available items:\n\n"
        + "1. Coal "+ " for " + str(CoalPrice) + "\n"
        + "2. Iron" + " for " + str(IronPrice) +"\n"
        + "3. " + UniqItem + " for " + str(UniqItemPrice) + "\n"
        + "4. Fuel for 1 unit per gallon")
    buy = input("\nChoose option:\n> ")

    if buy == "1":
        if userinfo.units < CoalPrice:
            print("Credit doesn't exist in space!")
        if userinfo.units >= CoalPrice:
            if userinfo.units >= (CoalPrice * 2):
                buymorethanone("Coal")
                if userinfo.units < (CoalPrice * number):
                    while not tryagain == "N" and not tryagain == "n" and (CoalPrice * number) > userinfo.units:
                        tryagain = input("You do not have enough units. \nWould you like to try again? (Y/N)\n\nChoose option:\n> ")
                        if tryagain == "y" or tryagain == "Y":
                            buymorethanone("Coal")
            if userinfo.units >= (CoalPrice * number): 
                userinfo.units -= (CoalPrice * number)
                userinfo.Coal += number
                print("You have purchased " + str(number) + " Coal for " + str(CoalPrice * number) )

    if buy == "2":
        if userinfo.units < IronPrice :
            print("Credit doesn't exist in space.")
        if userinfo.units >= IronPrice:
            if userinfo.units >= (IronPrice * 2):
                buymorethanone("Iron")
                if userinfo.units < (IronPrice * number):
                    while not tryagain == "n" and not tryagain == "N" and int(IronPrice * number) > userinfo.units:
                        tryagain = input("You do not have enough units. \nWould you like to try again? (Y/N)\n\nChoose option:\n> ")
                        if tryagain =="y" or tryagain == "Y":
                            buymorethanone("Iron")
            if userinfo.units >= (IronPrice * number):    
                userinfo.units -= int(IronPrice * number)
                userinfo.Iron += number
                print("You have purchased " + str(number) + " Iron for " + str(IronPrice * number))


    if buy == "3":
        if (userinfo.units - UniqItemPrice) < 0:
            print("Credit doesn't exist in space.")
        if userinfo.units > UniqItemPrice:
            if userinfo.units >= (UniqItemPrice * 2):
                buymorethanone(UniqItem)
                if userinfo.units < (UniqItemPrice * number):
                    while not tryagain == "n" and not tryagain == "N" and int(UniqItemPrice * number) > userinfo.units:
                        tryagain = input("You do not have enough units. \nWould you like to try again? (Y/N)\n\nChoose option:\n> ")
                        if tryagain == "Y" or tryagain == "y":
                            buymorethanone(UniqItem)
            userinfo.units -= UniqItemPrice * number 
            if UniqItem == "Diamond":
                userinfo.Diamond += number
            if UniqItem == "Flux Capacitor":
                userinfo.Flux_Capacitor += number
            if UniqItem == "Spongebob":
                userinfo.Spongebob += number
            print("You have purchased " + str(number) +" "+ UniqItem + " for " + str(UniqItemPrice * number))

    if buy == "4":
        os.system("clear")
        quantityfuel=input("How much fuel would you like to purchase?\n\nChoose quantity:\n> ")

        if not quantityfuel.isdigit():
            while not quantityfuel.isdigit():
                print("Invalid input detected. Please input a integer")
                quantityfuel=input("How much fuel would you like to purchase?\n\nChoose quantity:\n> ")

        quantityfuel = int(quantityfuel)
        if (userinfo.units - quantityfuel) <= 0:
            print("Credit doesn't exist in space.")

        if (userinfo.units - quantityfuel) >= 0:
            ship.current_fuel += quantityfuel
            userinfo.units -= quantityfuel

            if ship.current_fuel > 1000 and onetimeprint == 0:
                onetimeprint += 1
                print("Due to the extraordinary advancements of technology, The fuel tank expands to hold any amount of fuel!")
