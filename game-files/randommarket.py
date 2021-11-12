import userinfo
import sellmenu


items = ["1. Coal", "2. Iron", "3. Spongebob"]
prices = [200, 400, 800]


def listrandom():
    for p in range(3):
        print(items[p] + " for " +str(prices[p]) +"\n")


def randomsmarket():
    stay = "y"
    while stay == "y":
        print("Would you like to (b)uy or (s)ell?")
        marketans = input()
        if marketans == "b":
            listrandom()
            buy = input("Option>")
            if buy == "1":
                userinfo.units -= 200
                userinfo.Coal += 1
            if buy == "2":
                userinfo.units -= 400 
                userinfo.Iron += 1
            if buy == "3":
                userinfo.units -= 800
                userinfo.Spongebob += 1
              
              
        if marketans == "s":
            sellmenu.randomsell()
                    
        print("Would you like to continue? (Y,n)", end = "")
        stay = input()