import ship 
import planets
import userinfo
import os
import market
import story

onetime =0

def Main_loop():
    global onetime
    answer = 0
    while answer != "q" and answer != "Q":
        
        os.system("clear")
        units = userinfo.units
        print("               Player: " + story.user_name + '\n')
        print("               Planet: "+ ship.current_location_name)
        print("               Units: " + str(units))
        print("               Fuel: " + str(ship.current_fuel))
        print("               Age: "+ str(round(userinfo.age, 1)))
        print("\n        What would you like to do?\n"
             + "T for Travel                M for Market\n"
             + "I for Inventory             Q for Quit Game\n"
             + "\nChoose option:\n> ", end = "")
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
        if userinfo.units >= 50000 and onetime == 0:
            onetime += 1
            print(story.user_name + ", You have won!")
            contend = input("Would you like to continue? (Y,n")
            if contend == "n":
                answer = "q"
        if userinfo.age >= 62:
            print("Placeholder")
            answer = "q"


Main_loop()
print("Game Ended")
