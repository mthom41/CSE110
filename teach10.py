acc = []
balances = []
cont = True
total = 0

print("Enter the names and balances of bank accounts (type exit to finish)")

while cont:
    acc.append(input("What is the name of the account?: "))
    if acc[-1].lower() == "exit":
        acc.remove("exit")
        cont = False
        continue
    balances.append(float(input("What is the balance of the account?: ")))

print("Account information: ")
for i in acc:
    # This ugly little expression below just gets the index of i in the acc list and 
    # pulls the corresponding value from the balances list. 
    # It also does all that inside a print so even more fun
    print(i + " - $" + str(balances[acc.index(i)]))

for i in balances:
    total += i
print("Total Balance: $" + str(total))
print("Average Balance: $" + str(total/len(balances)))