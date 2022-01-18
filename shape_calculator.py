import math
# Define number checker
def check_input(num):
    try:
        num = float(num)
        return num
    except ValueError:
        print("Please input a number!")
        num = input("Number: ")
        return check_input(num)

# Define number cleanup
def cleanup(num):
    if num % 1 == 0:    
        return str(int(num))
    else:
        return str(num)

# Ask for inputs
print("Please input the following!")
square_side = check_input(input("Area of a square: "))
rect_s1 = check_input(input("Rectangle width: "))
rect_s2 = check_input(input("Rectangle length: "))
radius = check_input(input("Circle Radius: "))

# Do the math
square_area = square_side ** 2
rect_area = rect_s1 * rect_s2
circle_area = math.pi*(radius**2)

# print(square_area, rect_area, circle_area)
# (for debugging)

# Print everything
print("The area of your square is "+cleanup(square_area))
print("The area of your rectangle is "+cleanup(rect_area))
print("The area of your circle is "+cleanup(circle_area))