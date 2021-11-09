import stdrandom

# basic coordinates- Earth(0,0) Alpha Aproxima(0,-4.246) Random planet(a,b)

# define variable

starting_location = earth
earth_location = float([0,0])
alpha_aproxima_location = float([0,-4.246])

# define functions

def random_location():
    a = stdrandom.uniformFloat(-10,10)
    b = stdrandom.uniformFloat(-10,10)
    random_location = [a,b]
    return random_location

def current_location():
    return
