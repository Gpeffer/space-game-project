import stdrandom

# basic coordinates- Earth(0,0) Alpha Aproxima(0,-4.246) Random planet(a,b)

# define variables

earth_location = "[float(0), float(0)]"
alpha_aproxima_location = "[float(0), float(-4.246)]"

# define functions

def random_location():
    a = stdrandom.uniformFloat(-10,10)
    b = stdrandom.uniformFloat(-10,10)
    a = round(a, 3)
    b = round(b, 3)
    c = [float(a), float(b)]
    return c

random_planet_location = random_location()

print(random_planet_location)
