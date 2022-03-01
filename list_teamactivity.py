# initialize inputs
numlist = []
max = 0
summ = 0
av = 0
rept = True
inpt = 1

print("Enter a list of numbers. Enter 0 to finish")

while rept:
    inpt = int(input("Enter a number: "))
    if inpt == 0:
        rept = False
    else:
        numlist.append(inpt)

# Max finder
max = numlist[0]
for i in numlist:
    if i > max:
        max = i

print("The largest number is: " + str(max))

# Sum finder
for i in numlist:
    summ += i

print("The sum of the numbers is: " + str(summ))

# Average finder
av = summ/len(numlist)
print("The average of the numbers is: " + str(av))