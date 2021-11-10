import stdrandom

# basic coordinates- Earth(0,0) Alpha Aproxima(0,-4.246) Random planet(a,b)

# define variables

earth = [float(0.0), float(0.0)]
alpha_aproxima = [float(0), float(-4.246)]

# define functions

def random_location():
    a = stdrandom.uniformFloat(-10,10)
    b = stdrandom.uniformFloat(-10,10)
    a = round(a, 3)
    b = round(b, 3)
    c = [float(a), float(b)]
    return c
