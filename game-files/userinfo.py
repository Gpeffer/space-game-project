units = 1000 
age = 18.0
userinventory = []
def unitget(a):
    return units

def inventoryget():
    something = ""
    n=0
    for i in userinventory:
            n += 1
            something +=str(n)+ ". " + i + "\n"
    if something == "":
        return "You have nothing \n"
        return
    else: 
        return something
    
