# cline is cleaned line after splitting
cline = []
salary = 0
with open("hr_system.txt") as hr:

    print("HR Information")
    for line in hr:
        cline = line.split()
        salary = round(int(cline[3])/24, 2)
        if cline[2].lower() == "engineer":
            salary += 1000
        print(cline[0] + " (ID: " + cline[1] + "), " + cline[2] + " - $" + str(salary))
