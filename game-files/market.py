import userinfo
import Marketbuy
import Marketsell
import os

def market(currentlocation):
    stay = "y"
    while stay == "y" or stay == "Y":
        os.system("clear")
        bos = input("Would you like to (B)uy or (S)ell?\n\nChoose option:\n> ")

        if currentlocation == "Earth":
           
            if bos == "B" or bos == "b":
                os.system("clear")
                Marketbuy.buytemp("Diamond")
           
            if bos == "S" or bos == "s":
                os.system("clear")
                Marketsell.template()

        if currentlocation == "Alpha Aproxima":
           
            if bos == "B" or bos == "b":
                os.system("clear")
                Marketbuy.buytemp("Flux Capacitor")
           
            if bos == "S" or bos == "s":
                os.system("clear")
                Marketsell.template()
            
        if currentlocation == "Random Planet":

            if bos == "B" or bos == "b":
                os.system("clear")
                Marketbuy.buytemp("Spongebob")
            
            if bos == "S" or bos == "s":
                os.system("clear")
                Marketsell.template()
        stay = input("Would you like to stay in the market? (Y/N)\n\nChoose option:\n> ")
