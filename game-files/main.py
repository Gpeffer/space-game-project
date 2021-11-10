import ship 
import planets
import userinfo
import os
import market
def Not_yet():
    print("This has not yet been created or linked")
def Main_loop():
    answer = 0
    while answer != "q":
        os.system("clear")
        units = userinfo.units
        print("Units:" + str(units))
        print("Location:")
        print("What would you like to do?\n"
             + "t for Travel                m for Market\n"
             + "i for Inventory             q for Quit Game\n"
             + "Choice?  ", end = "")
        answer = input() 
        if answer == "t":
            os.system("clear")
            
        if answer == "m":
            os.system("clear")
            market.market("earth")
        if answer == "i":
            os.system("clear")
            print(userinfo.inventoryget(), end = "")
            print("Enter Any Key To Exit")
            input()


Main_loop()
print("Game Ended")