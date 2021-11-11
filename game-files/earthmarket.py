import userinfo


earthitems= ["1. Coal", "2. Iron", "3. Diamond"]
earthprices = [100, 250, 600]
earthsellprices = [100,250,600]


def listearth():
    for p in range(3):
        print(earthitems[p] + " for " +str(earthprices[p]) +"\n")


def earthsmarket():
    stay = "y"
    while stay == "y":
        print("Would you like to (b)uy or (s)ell?")
        marketans = input()
        if marketans == "b":
            listearth()
            buy = input("Option>")
            if buy == "1":
                userinfo.units -= earthprices[0]
                userinfo.userinventory += [earthitems[0][3:]]
            if buy == "2":
                userinfo.units -= earthprices[1]
                userinfo.userinventory += [earthitems[1][3:]]
            if buy == "3":
                userinfo.units -= earthprices[2]
                userinfo.userinventory += [earthitems[2][3:]]
             
              
        if marketans == "s":
            print(userinfo.inventoryget())
            print("What would you like to sell? ",end="")
            itemselector = input()
            if itemselector.isdigit():
                if (int(itemselector) - 1) < len(userinfo.userinventory):
                    sell = userinfo.userinventory[int(itemselector)- 1]
                    if sell == "Coal":
                        userinfo.units += 100
                        userinfo.userinventory.remove("Coal")
                    if sell == "Iron":
                        userinfo.units += 250
                        userinfo.userinventory.remove("Iron")
                    if sell == "Diamond":
                        userinfo.units += 600                                                                                                                                                                  
                        userinfo.userinventory.remove("Diamond") 
                    

        print("Would you like to continue? (Y,n)", end = "")
        stay = input()