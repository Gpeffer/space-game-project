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
    number = str(number)
    if number.isdigit():
        number = int(number)
        if number <= 0:
            print("Purchase Canceled")
        if number >= 1:
            return int(number)
    elif not number.isdigit():
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
    number = 1
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
        if userinfo.player.units < Marketsell.coalprice:
            print("Credit doesn't exist in space.")
        if userinfo.player.units >= Marketsell.coalprice and (userinfo.player.sumofinv() + 1) <= userinfo.player.invcap:
            if userinfo.player.units >= (Marketsell.coalprice* 2) and (userinfo.player.sumofinv()) + 2 <= userinfo.player.invcap:
                buymorethanone("Coal")

                if userinfo.player.units < (Marketsell.coalprice * number):
                   while not tryagain == "N" and not tryagain == "n" and (Marketsell.coalprice * number) > userinfo.player.units:
                        tryagain = input("You do not have enough units. \nWould you like to try again? (Y/N)\n\nChoose option:\n> ")
                        if tryagain == "y" or tryagain == "Y":
                            buymorethanone("Coal")

                if (userinfo.player.sumofinv() + number ) > userinfo.player.invcap:
                    while not tryagain == "N" and not tryagain == "n" and (userinfo.player.sumofinv() + number) > userinfo.player.invcap and (Marketsell.coalprice * number) > userinfo.player.units:
                        tryagain = input("You do not have enough space in Inventory? \nWould you like to try again? (Y/N)\n\nChoose option:\n> ")
                        if tryagain == "y" or tryagain == "Y":
                            buymorethanone("Coal")

            if userinfo.player.units >= (Marketsell.coalprice * number) and (userinfo.player.sumofinv() + number) <= userinfo.player.invcap: 
                userinfo.player.units -= (Marketsell.coalprice* number)
                userinfo.player.Coal += number
                os.system("clear")
                print("You have purchased " + str(number) + " Coal for " + str(Marketsell.coalprice* number) )

    if buy == "2":
        os.system("clear")
        if userinfo.player.units < Marketsell.ironprice:
            print("Credit doesn't exist in space.")
        if userinfo.player.units >= Marketsell.ironprice and (userinfo.player.sumofinv() + 1) <= userinfo.player.invcap:
            if userinfo.player.units >= (Marketsell.ironprice* 2) and (userinfo.player.sumofinv()) + 2 <= userinfo.player.invcap:
                buymorethanone("Iron")
                if userinfo.player.units < (Marketsell.ironprice * number):
                    while not tryagain == "n" and not tryagain == "N" and int(Marketsell.ironprice * number) > userinfo.player.units:
                        tryagain = input("You do not have enough units. \nWould you like to try again? (Y/N)\n\nChoose option:\n> ")
                        if tryagain =="y" or tryagain == "Y":
                            buymorethanone("Iron")

                if (userinfo.player.sumofinv() + number ) > userinfo.player.invcap:
                    while not tryagain == "N" and not tryagain == "n" and (userinfo.player.sumofinv() + number) > userinfo.player.invcap and (Marketsell.ironprice * number) > userinfo.player.units:
                        tryagain = input("You do not have enough space in Inventory? \nWould you like to try again? (Y/N)\n\nChoose option:\n> ")
                        if tryagain == "y" or tryagain == "Y":
                            buymorethanone("Iron")    

            if userinfo.player.units >= (Marketsell.ironprice* number)  and (userinfo.player.sumofinv() + number) <= userinfo.player.invcap:    
                userinfo.player.units -= int(Marketsell.ironprice* number)
                userinfo.player.Iron += number
                os.system("clear")
                print("You have purchased " + str(number) + " Iron for " + str(Marketsell.ironprice* number))


    if buy == "3":
        os.system("clear")
        if (userinfo.player.units - UniqItemPrice) < 0:
            print("Credit doesn't exist in space.")
        if userinfo.player.units > UniqItemPrice  and (userinfo.player.sumofinv() + 1) <= userinfo.player.invcap: 
            if userinfo.player.units >= (UniqItemPrice * 2) and (userinfo.player.sumofinv()) + 2 <= userinfo.player.invcap:
                buymorethanone(UniqItem)

                if userinfo.player.units < (UniqItemPrice * number):
                    while not tryagain == "n" and not tryagain == "N" and int(UniqItemPrice * number) > userinfo.player.units :
                        tryagain = input("You do not have enough units. \nWould you like to try again? (Y/N)\n\nChoose option:\n> ")
                        if tryagain == "Y" or tryagain == "y":
                            buymorethanone(UniqItem)

                if (userinfo.player.sumofinv() + number ) > userinfo.player.invcap:
                    while not tryagain == "N" and not tryagain == "n" and (userinfo.player.sumofinv() + number) > userinfo.player.invcap and (Marketsell.UniqItemPrice * number) > userinfo.player.units:
                        tryagain = input("You do not have enough space in Inventory? \nWould you like to try again? (Y/N)\n\nChoose option:\n> ")
                        if tryagain == "y" or tryagain == "Y":
                            buymorethanone(UniqItem)

        if userinfo.player.units >= (UniqItemPrice * number)  and (userinfo.player.sumofinv() + number) <= userinfo.player.invcap:
            userinfo.player.units -= UniqItemPrice * number 
            if UniqItem == "Diamond":
                userinfo.player.Diamond += number
            if UniqItem == "Flux Capacitor":
                userinfo.player.Flux_Capacitor += number
            if UniqItem == "Spongebob":
                userinfo.player.Spongebob += number
            os.system("clear")
            print("You have purchased " + str(number) +" "+ UniqItem + " for " + str(UniqItemPrice * number))

    if buy == "4":
        os.system("clear")
        print('Current fuel:', ship.current_fuel)
        buymorethanone("Fuel")
        if number > userinfo.player.units or number + ship.current_fuel > userinfo.player.maxfuel:
            while number > userinfo.player.units or number + ship.current_fuel > userinfo.player.maxfuel:
                os.system("clear")
                tryagain = input("Not enough units/Fuel Capacity. \n Would you like to try again?")
                if tryagain == "Y" or tryagain == "y":
                    buymorethanone("Fuel")
                if tryagain =="n" or tryagain == "N":
                    return
        if (userinfo.player.units - number) <= 0:
            os.system("clear")
            print("Credit doesn't exist in space.")
        
        if (userinfo.player.units - number) >= 0:
            ship.current_fuel += number
            userinfo.player.units -= number 
            print("You have purchased " + str(quantityfuel) +"gallons of fuel for " + str(quantityfuel))


