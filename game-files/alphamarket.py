import userinfo
import sellmenu


items = ["1. Coal", "2. Iron", "3. Flux Capacitor"]
prices = [150,300,900]



def listalpha():
    for p in range(3):
        print(items[p] + " for " + str(prices[p]) + "\n")


def alphasmarket():
      stay = "y"
      while stay == "y":
        print("Would you like to (b)uy or (s)ell?")
        marketans = input()
        if marketans == "b":
            listalpha()
            buy = input("Option>")
            if buy == "1":
                userinfo.units -= 150
                userinfo.Coal += 1
            if buy == "2":
                userinfo.units -= 300 
                userinfo.Iron += 1
            if buy == "3":
                userinfo.units -= 800
                userinfo.Flux_Capacitor += 1

        if marketans == "s":
            sellmenu.alphasell()
                    
        print("Would you like to continue? (Y,n)", end = "")
        stay = input()