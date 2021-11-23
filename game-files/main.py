import story
import userinfo
import ship 
import planets
import os
import market
import crime


onetime = 0

def Main_loop():
    global onetime
    global destruct
    global player
    answer = 0
    while answer != "q" and answer != "Q":
        
        os.system("clear")
        if ship.destruct == 1:
            break
        if crime.caught == 1:
            break
        
        print("                            Player: " + userinfo.player.name + '\n')
        print("                            Planet: "+ ship.current_location_name)
        print("                            Units: " + str(userinfo.player.units))
        print("                            Fuel: " + str(ship.current_fuel))
        print("                            Age: "+  str(userinfo.player.age))
        print("\n                    What would you like to do?\n"
             + "T for Travel                M for Market           S for Stats\n"
             + "I for Inventory             C for Crime            Q for Quit Game\n"
             + "\nChoose option:\n> ", end = "")
        answer = input() 

        if answer == "t" or answer == "T":
            os.system("clear")
            ship.travel_ui()
        
        elif answer == "m" or answer == "M":
            os.system("clear")
            market.market(ship.current_location_name)
        
        elif answer == "i" or answer == "I":
            os.system("clear")
            print(userinfo.inventoryget())
            input("\nPress Enter to exit.\n> ")
        elif answer == "c":
            crime.pickpocket()
        elif answer == "small loan of a million units":
            userinfo.player.units += 1000000
        elif userinfo.player.units >= 50000 and onetime == 0:
            onetime += 1
            print(userinfo.player.name + ", You have won!")
            contend = input("Would you like to continue? (Y,n")
            if contend == "n":
                answer = "q"
        elif userinfo.player.age >= 62:
            print("Placeholder")
            answer = "q"


Main_loop()
print("Game Ended")
