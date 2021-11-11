import ship 
import planets
import userinfo
import os
import market


def Main_loop():
    answer = 0
    while answer != "q":
        #os.system("clear")
        units = userinfo.units
        print("Age: "+ str(userinfo.age))
        print("Fuel: " + str(ship.current_fuel))
        print("Units:" + str(units))
        print("Location:"+ str(ship.current_location_name))
        print("What would you like to do?\n"
             + "t for Travel                m for Market\n"
             + "i for Inventory             q for Quit Game\n"
             + "Choice?  ", end = "")
        answer = input() 
        if answer == "t":
            os.system("clear")
            ship.travel_ui()
        if answer == "m":
            os.system("clear")
            market.market(ship.current_location_name)
        if answer == "i":
            os.system("clear")
            print(userinfo.inventoryget(), end = "")
            print("Enter Any Key To Exit")
            input()


Main_loop()
print("Game Ended")