# Initialize stuff
from hashlib import _BlakeHash


cart = []
costs = []
rept = True
item = " "
quant = 0
price = 0.0

# Define a recursive loop printer for testing
'''def loop_print(arg):
    for i in len(arg):
        print(arg[i])
'''

print("Welcome to your cart! Please add as many items as you want. Type 'done' as the item name to finish.")

while rept:
    item = input("Item name: ")
    if item.lower() == "done":
        rept = False
        break
    cart.append(item)
    quant = int(input("Quantity (leave blank if 1): "))
    price = float(input("Price per item: "))
    price = price*quant
    costs.append(price)

#loop_print(cart)
#loop_print(costs)
print(cart)
print(costs)