import userinfo
import sellmenu


items= ["1. Coal", "2. Iron", "3. Diamond"]
prices = [100, 250, 600]



def listearth():
    for p in range(3):
        print(items[p] + " for " +str(prices[p]) +"\n")


def earthsmarket():
    stay = "y"
    while stay == "y":
        print("Would you like to (b)uy or (s)ell?")
        marketans = input()
        if marketans == "b":
            listearth()
            buy = input("Option>")
            if buy == "1":
                userinfo.units -= 100
                userinfo.Coal += 1
            if buy == "2":
                userinfo.units -= 250 
                userinfo.Iron += 1
            if buy == "3":
                userinfo.units -= 600
                userinfo.Diamond += 1
             
              
        if marketans == "s":
            sellmenu.earthsell()
                    
        print("Would you like to continue? (Y,n)", end = "")
        stay = input()