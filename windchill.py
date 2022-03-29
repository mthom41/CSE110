import math
def compute_chill(temp, speed):
    result = 35.74 + (0.6215*temp) - ((35.75)*(speed**0.16)) + ((0.4275 * temp)*(speed**0.16))
    result = round(result, 2)
    return result
temp_range = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
temperature = 0
chill = 0

temperature = float(input("What is the temperature?: "))
if input("Fahrenheit or Celsius (F/C)?: ").lower() == "c":
    temperature = (temperature*9)/5 + 32

for tmp in temp_range:
    chill = compute_chill(temperature, tmp)
    print("At a temperature of " + str(temperature) + "F, and a wind speed of " + str(tmp) + "mph, the windchill is: " + str(chill) + "F")