import ship 
import planets
import userinfo
def Not_yet():
    print("This has not yet been created or linked")
def Main_loop():
    answer = 0
    while answer != "q":
        units = userinfo.unitget(1)
        print("Units:" + str(units))
        print("Location:")
        print("What would you like to do?\n"
             + "t for Travel\n"
             +  "m for Market\n"
             +  "i for Inventory")   
        answer = input() 
        if answer == "t":
            Not_yet()
        if answer == "m":
            Not_yet()
        if answer == "i":
            Not_yet()


Main_loop()
print("Game Ended")