# Meal Price Calculator

# Define a function that ensures an input is a number
def num_input(message):
    num = input(message)
    try:
        num = float(num)
        return num
    except ValueError:
        print("Please input a number!")
        return num_input(message)

# Define a fundtion requiring adequate payment
def checkpayment(message, req):
    pay=num_input(message)
    if pay<req:
        print("That's not enough! Please change the amount and try again.")
        return checkpayment(message, req)
    else:
        print("Paid: $" + str("{:.2f}".format(pay)))
        print("Change: $" + str("{:.2f}".format(pay-req))
        return True

# Get user input
print("Please input the following")
kidmeal = num_input("Price of a children's meal: ")
adultmeal = num_input("Price of an adult's meal: ")
kids = num_input("Number of children: ")
adults = num_input("Number of adults: ")
taxrate = num_input("Sales tax rate (as a percentage): ")

# Math everything
subtotal = (kidmeal*kids) + (adultmeal*adults)
tax = subtotal*(taxrate/100)
total = subtotal+tax

#  Print totals at 2 decimal places
print("Subtotal: $"+str("{:.2f}".format(subtotal)))
print("Tax: $"+str("{:.2f}".format(tax)))
print("Total: $"+str("{:.2f}".format(total)))

# Check that the payment is enough and return payment and change info
checkpayment("Payment amount: ", total)