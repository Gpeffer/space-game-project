units = 1000 
age = 18.0
Coal = 0
Iron = 0
Diamond = 0 
Flux_Capacitor = 0
Spongebob = 0

def inventoryget():
    print("1. Coal:" + str(Coal))
    print("2. Iron:" + str(Iron))
    print("3. Diamond:"+ str(Diamond))
    print("4. Flux Capacitor:"+ str(Flux_Capacitor))
    print("5. Spongebob:"+ str(Spongebob))

def inventorygetforsell(Coalp, Ironp, Diamondp, Flux_Capacitorp, Spongebobp):
    print("1. Coal: " + str(Coal) + " for " + str(Coalp) + " a piece")
    print("2. Iron: " + str(Iron)+ " for " + str(Ironp) + " a piece")
    print("3. Diamond: "+ str(Diamond) + " for " +str(Diamondp) + " a piece")
    print("4. Flux Capacitor: "+ str(Flux_Capacitor)+ " for " + str(Flux_Capacitorp) + " a piece")
    print("5. Spongebob: "+ str(Spongebob)+ " for " + str(Spongebobp) + " a piece")

