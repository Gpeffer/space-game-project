import userinfo
import Marketbuy
import Marketsell
import os
#buytemp(Uniqitem, coal price, ironprice, uniqitem price)
#selltemp(coal price, iron price, diamond price, flux capacitor price, spongebob price)

def market(currentlocation):
    stay = "y"
    while stay == "y" or stay == "Y":
        os.system("clear")
        bos = input("Would you like to (B)uy or (S)ell? \n>")

        if currentlocation == "Earth":
           
            if bos == "B" or bos == "b":
                Marketbuy.buytemp("Diamond",100, 250, 600)
           
            if bos == "S" or bos == "s":
                Marketsell.template(100,250,600,1400,1200)

        if currentlocation == "Alpha Aproxima":
           
            if bos == "B" or bos == "b":
                Marketbuy.buytemp("Flux Capacitor",150, 300, 900)
           
            if bos == "S" or bos == "s":
                Marketsell.template(150,250,900,800,1300)
            
        if currentlocation == "Random Planet":

            if bos == "B" or bos == "b":
                Marketbuy.buytemp("Spongebob", 200, 400, 800)
            
            if bos == "S" or bos == "s":
                Marketsell.template(200,400,1400,1600,800)
        stay = input("Would you like to stay in the market?")