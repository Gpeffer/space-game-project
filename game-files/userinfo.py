from story import user_name
class user:
    def __init__ (self,Name):
        self.name= Name
        self.units = 1000 
        self.age = 18.0
        self.Coal = 0
        self.Iron = 0
        self.Diamond = 0 
        self.Flux_Capacitor = 0
        self.Spongebob = 0
        self.invcap = 5
        self.maxfuel = 100
    def sumofinv(self):
        return self.Diamond + self.Flux_Capacitor + self.Spongebob + self.Coal + self.Iron
player = user(user_name)
def inventoryget():
    print("   Iventory:\n")
    print("Coal: " + str(player.Coal))
    print("Iron: " + str(player.Iron))
    print("Diamond: "+ str(player.Diamond))
    print("Flux Capacitor: "+ str(player.Flux_Capacitor))
    return "Spongebob: " + str(player.Spongebob)

def inventorygetforsell(Coalp, Ironp, Diamondp, Flux_Capacitorp, Spongebobp):
    print("1. Coal: " + str(player.Coal) + " for " + str(Coalp) + " a piece")
    print("2. Iron: " + str(player.Iron)+ " for " + str(Ironp) + " a piece")
    print("3. Diamond: "+ str(player.Diamond) + " for " +str(Diamondp) + " a piece")
    print("4. Flux Capacitor: "+ str(player.Flux_Capacitor)+ " for " + str(Flux_Capacitorp) + " a piece")
    print("5. Spongebob: "+ str(player.Spongebob)+ " for " + str(Spongebobp) + " a piece")

