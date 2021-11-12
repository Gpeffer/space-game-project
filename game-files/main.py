import ship 
import planets
import userinfo
import os
import market


def Main_loop():
    answer = 0
    while answer != "q" and answer != "Q":
        
        os.system("clear")
        units = userinfo.units
        
        print("Age:   "+ str(round(userinfo.age,2)))
        print("Fuel:  " + str(round(ship.current_fuel, 2)))
        print("Units: " + str(units))
        print("What would you like to do?\n"
             + "T for Travel                M for Market\n"
             + "I for Inventory             Q for Quit Game\n"
             + "Choice?  ", end = "")
        answer = input() 
       
        if answer == "t" or answer == "T":
            os.system("clear")
            ship.travel_ui()
        
        if answer == "m" or answer == "M":
            os.system("clear")
            market.market(ship.current_location_name)
        
        if answer == "i" or answer == "I":
            os.system("clear")
            print(userinfo.inventoryget())
            print("Enter Any Key To Exit")
            input()


Main_loop()
print("Game Ended")