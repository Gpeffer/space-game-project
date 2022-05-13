# import modules

import stdrandom

# define functions

def random_location():
    a = stdrandom.uniformFloat(-10,10)
    b = stdrandom.uniformFloat(-10,10)
    a = round(a, 3)
    b = round(b, 3)
    c = [float(a), float(b)]
    return c

# define variables

earth_location = [float(0.0), float(0.0)]
alpha_location = [float(0), float(-4.246)]
random_planet_location = random_location()

a
