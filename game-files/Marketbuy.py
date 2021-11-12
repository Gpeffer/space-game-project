import userinfo
import ship

somethingrandom = 0

def buytemp(UniqItem, CoalPrice, IronPrice, UniqItemPrice):
    global somethingrandom
    print("1. Coal "+ " for " + str(CoalPrice) + "\n"
        + "2. Iron" + " for " + str(IronPrice) +"\n"
        + "3. " + UniqItem + " for " + str(UniqItemPrice) + "\n"
        + "4. Fuel for 1 unit per gallon")
    buy = input("Option>")

    if buy == "1":
         userinfo.units -= 200
         userinfo.Coal += 1

    if buy == "2":
        userinfo.units -= 400 
        userinfo.Iron += 1

    if buy == "3":
        userinfo.units -= 800
        userinfo.Spongebob += 1

    if buy == "4":
        quantityfuel=input("How much fuel would you like to purchase?  ")

        if not quantityfuel.isdigit():
            while not quantityfuel.isdigit():
                print("Invalid input detected. Please input a integer")
                quantityfuel=input("How much fuel would you like to purchase?  ")

        quantityfuel = int(quantityfuel)
        if (userinfo.units - quantityfuel) <= 0:
            print("Credit doesn't exist in space.")

        if (userinfo.units - quantityfuel) >= 0:
            ship.current_fuel += quantityfuel
            userinfo.units -= quantityfuel
                    
            if ship.current_fuel > 1000 and somethingrandom == 0:
                somethingrandom += 1
                print("Due to the extraordinary advancements of technology, The fuel tank expands to hold any amount of fuel!")