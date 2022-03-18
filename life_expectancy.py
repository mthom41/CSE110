'''plan
initialize stuff
open file
for every line
    compare life expectancy to highest and lowest
    if it's higher or lower, replace appropriately
    # replace country names and years as well (later in project)

'''
#set up some veriables?
min_exp = 100
min_cont = ""
min_year = 0
max_exp = 0
max_cont = ""
max_year = 0
inp_year = 0
total = 0
avg = 0
years = 0
inp_max = 0
inp_max_cont = ""
inp_min = 100
inp_min_cont = ""

with open("life_expectancy.csv") as datta:
    inp_year = int(input("Please select a year of interest: "))
    header=next(datta)
    for line in datta:
        line = line.strip()
        line = line.split(",")
        if float(line[3]) < min_exp:
            min_exp=float(line[3])
            min_cont=line[0]
            min_year=line[2]
        elif float(line[3]) > max_exp:
            max_exp = float(line[3])
            max_cont=line[0]
            max_year=line[2]
        if int(line[2]) == inp_year:
            total += float(line[3])
            years += 1
            if float(line[3]) < inp_min:
                inp_min = float(line[3])
                inp_min_cont = line[0]
            elif float(line[3]) > inp_max:
                inp_max = float(line[3])
                inp_max_cont = line[0]
    avg = total/years
        
print("The highest historical life expectancy is " + str(max_exp) + " in " + max_cont + " in the year " + max_year)
print("The lowest historical life expectancy is " + str(min_exp) + " in " + min_cont + " in the year " + min_year)
print("")
print("In " + str(inp_year) + " the average life expectancy was " + str(avg))
print("The highest life expectancy was " + str(inp_max) + " in " + inp_max_cont)
print("The lowest life expectancy was " + str(inp_min) + " in " + inp_min_cont)

    