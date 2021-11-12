import ship 
import planets
import userinfo
import os
import market
import story


def Main_loop():
    answer = 0
    while answer != "q" and answer != "Q":
        
        os.system("clear")
        units = userinfo.units
        print("               Planet: "+ ship.current_location_name)
        print("               Units: " + str(units))
        print("               Fuel: " + str(ship.current_fuel))
        print("               Age: "+ str(round(userinfo.age, 1)))
        print("        What would you like to do?\n"
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
            input("Press Enter to exit.\n")
            
        if answer == "small loan of a million units":
            userinfo.units += 1000000


Main_loop()
print("Game Ended")
