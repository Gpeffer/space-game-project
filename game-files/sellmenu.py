import userinfo 


noitem = "You can't sell hopes and dreams!"
itemexists = "Thank you for your business."


def template(coalprice,ironprice,diamondprice,Flux_Capacitorprice,Spongebobprice):

    userinfo.inventorygetforsell(coalprice,ironprice,diamondprice,Flux_Capacitorprice,Spongebobprice)
    option = input("Input Number of item you wish to sell. \n >")

    if option == "1":

        if userinfo.Coal == 0:
            print(noitem)

        if userinfo.Coal > 0:
            userinfo.Coal -= 1
            userinfo.units += coalprice
            print(itemexists)

    if option == "2":

        if userinfo.Iron == 0:
            print(noitem)

        if userinfo.Iron > 0:
            userinfo.Iron -= 1
            userinfo.units += ironprice
            print(itemexists)

    if option == "3":

        if userinfo.Diamond == 0:
            print(noitem)

        if userinfo.Diamond > 0:
            userinfo.Diamond -= 1
            userinfo.units += diamondprice

    if option == "4":

        if userinfo.Flux_Capacitor == 0:
            print(noitem)

        if userinfo.Flux_Capacitor > 0:
            userinfo.Flux_Capacitor -= 1
            userinfo.units += Flux_Capacitorprice

    if option == "5":

        if userinfo.Spongebob == 0:
            print(noitem)

        if userinfo.Spongebob > 0:
            userinfo.Spongebob -= 1
            userinfo.units += Spongebobprice
            print(itemexists)

def earthsell(): 
    template(100,250,600,1400,1200)

def alphasell():
    template(150,250,900,800,1300)

def randomsell():
    template(200,400,1400,1600,800)