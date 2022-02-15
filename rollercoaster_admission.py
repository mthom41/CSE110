age1 = int(input("What is the age of the first rider?:\n"))
height1 = int(input("What is the height of the first rider in inches?: \n"))
second_rider = input("IS there a second rider? (y/n)").lower()
if second_rider == "y":
    age2 = int(input("What is the age of the second rider?: \n"))
    height2 = int(input("What is the height of the second rider?: \n"))
#cover cases with a single rider(pretty easy)
if second_rider == "n":
    if height1 >= 62 and age1 >= 18:
        print("You may ride.")
    else:
        print("Sorry, you may not ride.")
# now it gets fun
# eliminate cases that auto-stop people first
elif second_rider == "y":
    if (height1 < 36) or (height2 < 36):
        print("Sorry, you cannot ride.")
    # stretch exception for two under-18 riders
    elif (age1 < 18) and (age2 < 18):
        if ((age1 and age2) >= 12) and ((height1 and height2) >= 52):
            print("You may ride")
        else:
            print("Sorry, you cannot ride.")
    # already knowing both riders are over the height limit, 
    # as long as one of them is 18+ yrs it's cool.
    elif (age1>=18) or (age2>=18):
        print("You may ride.")
    # I don't think I missed any cases but just in case
    else: 
        print("You may not ride")