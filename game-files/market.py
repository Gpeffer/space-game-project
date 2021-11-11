import userinfo
import earthmarket
import alphamarket
import randommarket
random_planet = ["1. Coal", "2. Iron", "3. Spongebob"]
alpha_aproxima = ["1. Coal", "2. Iron", "3. Flux Capicator"]

def market(currentlocation):
    global units
    global userinventory
    if currentlocation == "Earth":
        earthmarket.earthsmarket() 
    if currentlocation == "":
        alphamarket.alphamarket()
    if currentlocation == "random_planet":
        randommarket.randommarket()