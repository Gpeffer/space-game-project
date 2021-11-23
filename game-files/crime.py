import userinfo 
import random
import os 
import Marketsell
caught = 0
def theftfail(msp, item):
        global caught
        global deathawaits
        os.system("clear")
        deathawaits = False

        print("You have failed to acquire "+item+".") 

        if  userinfo.player.units < msp:
            print("You don't have enough money.\n"
                + "Your existence has been terminated.")
            caught = 1
            deathawaits = True

        else:
            print("You have been charged the going rate for "+item +"!")
            userinfo.player.units -= msp
            input("Press Enter to continue.")
                
def pickpocket():
    os.system("clear")

    randomperson = userinfo.user("randomperson")
    randomperson.Coal = random.randint(0,1)
    randomperson.Iron = random.randint(0,1)
    randomperson.Diamond = random.randint(0,1)
    randomperson.Flux_Capacitor = random.randint(0,1)
    randomperson.Spongebob = random.randint(0,1)

    answer = input("WARNING: Unsuccesfull theft will result in charge of current price.\n"
                +  " Inability to pay will result in death.\n"
                +  "Are you sure you want to steal? (Y/N)")

    if answer == "Y" or answer == "y":
        os.system("clear")
        repeat = False

        while not repeat:
            os.system("clear")
            chance = random.randint(0,1)

            itempick = input("Items\n"
            + "\n1. Coal: " + str(randomperson.Coal)
            + "\n2. Iron: " + str(randomperson.Iron)
            + "\n3. Diamond: " + str(randomperson.Diamond)
            + "\n4. Flux Capacitor: " + str(randomperson.Flux_Capacitor)
            + "\n5. Spongebob: " + str(randomperson.Spongebob)
            + "\nItem Number to steal or E to exit.")
            
            if itempick == "1":
                if randomperson.Coal == 0:
                    print("You can't steal what doesn't exist!")
                elif chance == 1:
                    userinfo.player.Coal += randomperson.Coal
                    os.system("clear")
                    print("You have tactically acquired Coal.")
                    randomperson.Coal -= 1
                    input("Press Enter to Continue.")
                elif chance == 0:
                    theftfail(Marketsell.coalprice,"Coal")
                    if deathawaits:
                        break

            elif itempick == "2":
                if randomperson.Iron == 0:
                    print("You can't steal something that doesn't exist!")
                elif chance == 1:
                    userinfo.player.Iron += randomperson.Iron
                    os.system("clear")
                    print("You have tactically acquired Iron.")
                    randomperson.Iron -= 1             
                    input("Press Enter to Continue.")
                elif chance == 0:
                    theftfail(Marketsell.ironprice, "Iron")
                    if deathawaits:
                        break 

            elif itempick == "3":
                if randomperson.Diamond == 0:
                    print("You cant steal something that doesn't exist!")
                elif chance == 1:
                    userinfo.player.Diamond += randomperson.Diamond
                    os.system("clear")
                    print("You have tactically acquired Diamond.")
                    randomperson.Diamond -= 1
                    input("Press Enter to Continue.")
                elif chance == 0:
                    theftfail(Marketsell.diamondprice, "Diamond" )
                    if deathawaits:
                        break

            elif itempick == "4":
                if randomperson.Flux_Capacitor == 0:
                    print("You can't steal something that doesn't exist!")
                elif chance == 1:
                    userinfo.player.Flux_Capacitor += randomperson.Flux_Capacitor
                    os.system("clear")
                    print("You have tactically acquired a Flux Capacitor")
                    randomperson.Flux_Capacitor -= 1
                    input("Press Enter to Continue.")
                elif chance == 0:
                    theftfail(Marketsell.Flux_Capacitorprice, "Flux Capacitor")
                    if deathawaits:
                        break

            elif itempick == "5":
                if randomperson.Spongebob == 0:
                    print("You can't steal something that doesn't exist!")
                elif chance == 1:
                    userinfo.player.Spongebob += randomperson.Spongebob
                    os.system("clear")
                    print("You have tactically acquired Spongebob")
                    randomperson.Spongebob -= 1
                    input("Press Enter to Continue.")
                elif chance == 0:
                    theftfail(Marketsell.Spongebobprice, "Spongebob")
                    if deathawaits:
                        break

            elif itempick == "E" or itempick == "e":
                break

            else: 
                itempick = input("Invalid Input, Try again or E for exit.")
                if itempick == "E" or itempick == "e":
                    break

    elif answer == "N" or answer == "n":
        print("test")

            