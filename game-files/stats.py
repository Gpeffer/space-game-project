import userinfo
import os

def Stats():
    os.system("clear")
    while True: 
        upgexit= input("1. Inventory Cap: " + str(userinfo.player.invcap) + " (Increase by 5 for 100)"
                +  "\n2. Max Fuel Cap: " + str(userinfo.player.maxfuel) + " (Increase by 50 for 100)"
                +  "\n Number of item to Upgrade or Enter to Exit\n"
                +  ">")
        if upgexit == "1":
            if userinfo.player.units >= 100:
                userinfo.player.invcap += 5
                userinfo.player.units -= 100
                print("Max Fuel Upgraded")
            else:
                print("Credit doesn't exist in space!")
        elif upgexit == "2":
            if userinfo.player.units >= 100:
                userinfo.player.maxfuel += 50
                userinfo.player.units -= 100
                print("Max Fuel Upgraded")
            else:
                print("Credit doesn't exist in space!")
        else:
            break 
