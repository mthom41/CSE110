# Namebadge generator. Just basic strings at the moment

# Collect Inputs
import email


name_first = input("What's your first name?: ")
name_last = input("What is your last name?: ")
title = input("What's your title?: ").capitalize()
id = input("What's your ID number?: ")

emmail = input("What's your email address?: ")
phone = input("What's your phone number?: ")
'''
hair = input("What is your hair color?: ")
eyes = input("What is your eye color?: ")
month = input("What month did you begin your employment?: ")
training = input("Have you undergone specialized training?: ")'''

# Return and display inputs as a name badge
print("------------------------------")
print(name_last.upper() + ", "+name_first.upper())
print(f'{title}')
print("ID: "+id+"\n")

print(emmail)
print(phone)
print("------------------------------")