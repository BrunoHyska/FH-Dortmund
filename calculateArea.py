from math import pi


def calculate_area():
    radius = input("Write the radius: ")
    if radius.isnumeric():
        rad = float(radius)
        area = 2 * pi * rad
        print(area)
    else:
        print("Only numbers are allowed")
        calculate_area()

calculate_area()


