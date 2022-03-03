# Initialize stuff
cart = []
costs = []
rept = True
item = " "
quant = 0
price = 0.0
rmv = " "

# Define a recursive loop printer for testing
def list_print(arg):
    for item in arg:
        print(item)

# Define a list adder
def addlist(list):
    list_total = 0
    for i in list:
        list_total += i
    return list_total

print("Welcome to your cart! Please add as many items as you want. Commands: 'done', 'remove' ")

while rept:
    item = input("Item name: ")
    if item.lower() == "done":
        rept = False
        break
    if item.lower() == "remove":
        print("Cart: ")
        list_print(cart)
        rmv = input("Which item would you like to remove?: ")
        if rmv in cart:
            # This line is a bit crazy. basically it finds the index of whatever item 
            # we're removing and matches that value in the list of costs
            # It reads better from right to left haha
            print(rmv + " price is " + str(costs[cart.index(rmv)]))
            if input("Remove? y/n ").lower() == "y":
                # This line uses the same process to remove the corresponding cost from the appropriate list
                del costs[cart.index(rmv)]
                cart.remove(rmv)
                continue
            else:
                print(rmv + " not deleted.")
                continue
        else:
            continue
    cart.append(item)
    quant = int(input("Quantity (leave blank if 1): ") or 1)
    price = float(input("Price per item: "))
    price = price*quant  
    costs.append(price)
    print(cart)
    print(costs)   

#loop_print(cart)
#loop_print(costs)

print("Items: ")
list_print(cart)
print("Total: $" + str(addlist(costs)))