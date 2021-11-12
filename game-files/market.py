import userinfo
import earthmarket
import alphamarket
import randommarket

def market(currentlocation):
    if currentlocation == "Earth":
        earthmarket.earthsmarket() 
    if currentlocation == "Alpha Aproxima":
        alphamarket.alphasmarket()
    if currentlocation == "Random Planet":
        randommarket.randommarket()