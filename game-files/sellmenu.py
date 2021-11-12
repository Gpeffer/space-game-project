import userinfo 


noitem = "You can't sell hopes and dreams!"
itemexists = "Thank you for your business."


def earthsell(): 

    userinfo.inventorygetforsell(100,250,600,1400,1200)
    option = input("Input Number of item you wish to sell. \n >")

    if option == "1":

        if userinfo.Coal == 0:
            print(noitem)

        if userinfo.Coal > 0:
            userinfo.Coal -= 1
            userinfo.units += 100
            print(itemexists)

    if option == "2":

        if userinfo.Iron == 0:
            print(noitem)

        if userinfo.Iron > 0:
            userinfo.Iron -= 1
            userinfo.units += 250
            print(itemexists)

    if option == "3":

        if userinfo.Diamond == 0:
            print(noitem)

        if userinfo.Diamond > 0:
            userinfo.Diamond -= 1
            userinfo.units += 600

    if option == "4":

        if userinfo.Flux_Capacitor == 0:
            print(noitem)

        if userinfo.Flux_Capacitor > 0:
            userinfo.Flux_Capacitor -= 1
            userinfo.units += 1200

    if option == "5":

        if userinfo.Spongebob == 0:
            print(noitem)

        if userinfo.Spongebob > 0:
            userinfo.Spongebob -= 1
            userinfo.units += 1400
            print(itemexists)

def alphasell():

    userinfo.inventorygetforsell(150,250,900,800,1300)
    option = input("Input Number of item you wish to sell. \n >")

    if option == "1":

        if userinfo.Coal == 0:
            print(noitem)

        if userinfo.Coal > 0:
            userinfo.Coal -= 1
            userinfo.units += 150
            print(itemexists)

    if option == "2":

        if userinfo.Iron == 0:
            print(noitem)

        if userinfo.Iron > 0:
            userinfo.Iron -= 1
            userinfo.units += 300
            print(itemexists)

    if option == "3":

        if userinfo.Diamond == 0:
            print(noitem)

        if userinfo.Diamond > 0:
            userinfo.Diamond -= 1
            userinfo.units += 900

    if option == "4":
        if userinfo.Flux_Capacitor == 0:
            print(noitem)
        if userinfo.Flux_Capacitor > 0:
            userinfo.Flux_Capacitor -= 1
            userinfo.units += 800

    if option == "5":

        if userinfo.Spongebob == 0:
            print(noitem)

        if userinfo.Spongebob > 0:
            userinfo.Spongebob -= 1
            userinfo.units += 1300
            print(itemexists)

   


    

    
