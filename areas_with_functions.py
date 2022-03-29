import math

side_inp0 = 0
side_inp1 = 0
radius = 0
area = 0

def compute_rect(side1, side2):
    return side1*side2

def compute_circle(rad):
    return ((rad**2)*math.pi)

def compute_square(side):
    return side*side

print("Welcome to the new and improved shape area calculator.")
# square
side_inp1 = float(input("Input the side length of a square: "))
area = compute_square(side_inp1)
print("The area of that square is " + str(area))
# rectangle
side_inp0 = float(input("Please input side 1 of a rectangle: "))
side_inp1 = float(input("PLease input side 2 of a reectangle: "))
area = compute_rect(side_inp0, side_inp1)
print("The area of the rectangle is " + str(area))
# circle
radius = float(input("Please input the radius of a circle: "))
area = compute_circle(radius)
print("The area of the circle is " + str(area))
