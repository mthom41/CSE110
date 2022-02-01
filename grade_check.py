# Get user input

perc = float(input("What percent do you have in the class right now?"))
grade=""

# Determine letter value
if perc >= 90:
    grade = "A"
elif perc >= 80 and perc < 90:
    grade = "B"
elif perc >= 70 and perc < 80:
    grade = "C"
elif perc >= 60 and perc < 70:
    grade = "D"
elif perc < 60:
    grade = "F"

if grade != "F":
    if (perc % 10) >= 7:
        grade += "+"
print("Your grade in the class is: "+grade)
