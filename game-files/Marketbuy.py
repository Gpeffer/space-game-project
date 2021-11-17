import userinfo
import ship
import os
import Marketsell
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


def buytemp(UniqItem):
    global onetimeprint
    global number
    global items
    global units
    curloc = ship.current_location_name
    if curloc == "Earth":
        UniqItemPrice = Marketsell.diamondprice
    if curloc == "Alpha Aproxima":
        UniqItemPrice = Marketsell.Flux_Capacitorprice
    if curloc == "Random Planet":
        UniqItemPrice = Marketsell.Spongebobprice
    tryagain = "Placeholder"
    print("Available items:\n\n"
        +"1. Coal "+ " for " + str(Marketsell.coalprice) + "\n"
        + "2. Iron" + " for " + str(Marketsell.ironprice) +"\n"
        + "3. " + UniqItem + " for " + str(UniqItemPrice) + "\n"
        + "4. Fuel for 1 unit per gallon")
    buy = input("\nChoose option:\n> ")

    if buy == "1":
        os.system("clear")
        if userinfo.units < Marketsell.coalprice:
            print("Credit doesn't exist in space.")
        if userinfo.units >= Marketsell.coalprice:
            if userinfo.units >= (Marketsell.coalprice* 2):
                buymorethanone("Coal")
                if userinfo.units < (Marketsell.coalprice * number):
                    while not tryagain == "N" and not tryagain == "n" and (Marketsell.coalprice * number) > userinfo.units:
                        tryagain = input("You do not have enough units. \nWould you like to try again? (Y/N)\n\nChoose option:\n> ")
                        if tryagain == "y" or tryagain == "Y":
                            buymorethanone("Coal")
            if userinfo.units >= (Marketsell.coalprice* number): 
                userinfo.units -= (Marketsell.coalprice* number)
                userinfo.Coal += number
                os.system("clear")
                print("You have purchased " + str(number) + " Coal for " + str(Marketsell.coalprice* number) )

    if buy == "2":
        os.system("clear")
        if userinfo.units < Marketsell.ironprice:
            print("Credit doesn't exist in space.")
        if userinfo.units >= Marketsell.ironprice:
            if userinfo.units >= (Marketsell.ironprice* 2):
                buymorethanone("Iron")
                if userinfo.units < (Marketsell.ironprice * number):
                    while not tryagain == "n" and not tryagain == "N" and int(Marketsell.ironprice * number) > userinfo.units:
                        tryagain = input("You do not have enough units. \nWould you like to try again? (Y/N)\n\nChoose option:\n> ")
                        if tryagain =="y" or tryagain == "Y":
                            buymorethanone("Iron")
            if userinfo.units >= (Marketsell.ironprice* number):    
                userinfo.units -= int(Marketsell.ironprice* number)
                userinfo.Iron += number
                os.system("clear")
                print("You have purchased " + str(number) + " Iron for " + str(Marketsell.ironprice* number))


    if buy == "3":
        os.system("clear")
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
            os.system("clear")
            print("You have purchased " + str(number) +" "+ UniqItem + " for " + str(UniqItemPrice * number))

    if buy == "4":
        os.system("clear")
        print('Current fuel:', ship.current_fuel)
        quantityfuel=input("\nHow much fuel would you like to purchase?\n\nChoose quantity:\n> ")

        if not quantityfuel.isdigit():
            while not quantityfuel.isdigit():
                os.system("clear")
                print("Invalid input detected. Please input a integer")
                quantityfuel=input("How much fuel would you like to purchase?\n\nChoose quantity:\n> ")

        quantityfuel = int(quantityfuel)
        if (userinfo.units - quantityfuel) <= 0:
            os.system("clear")
            print("Credit doesn't exist in space.")

        if (userinfo.units - quantityfuel) >= 0:
            ship.current_fuel += quantityfuel
            userinfo.units -= quantityfuel
            print("You have purchased " + str(quantityfuel) +"gallons of fuel for " + str(quantityfuel))

            if ship.current_fuel > 1000 and onetimeprint == 0:
                onetimeprint += 1
                print("Due to the extraordinary advancements of technology, The fuel tank expands to hold any amount of fuel!")
