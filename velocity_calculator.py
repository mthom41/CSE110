import math

# Take user input
print("Hello! Welcome to the velocity calculator. Please input the following information.")

mass = float(input("Mass (in kg): "))
gravity = float(input("Gravitational acceleration (in m/s^2, 9.8 is earth's): "))
time = float(input("Time elapsed (in seconds): "))
density = float(input("Density of surrounding fluid (in kg/m^3, 1.3 is air and 1000 is water): "))
cross_section_a = float(input("Cross-sectional area (in m^2): "))
drag_c = float(input("Drag constant (0.5 for a sphere, 1.1 for a cylinder): "))

# Calculate 'c' from existing values then do the rest of the math
mysterious_c = 1/(2*(density*cross_section_a*drag_c))
velocity = math.sqrt((mass*gravity)/mysterious_c)*(1-math.exp((-math.sqrt(mass*gravity*mysterious_c)/mass)*time))

# Print results
print("The internal value of c is "+format(mysterious_c, ".3f"))
print("the velocity of the object at "+str(time)+" seconds is "+format(velocity, ".2f")+"m/s")
