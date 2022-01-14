import math


def paint_calc(height,width, cover ):
    area = height*width
    cans = math.ceil(area / cover)
    print(f"You'll need {cans} cans of paint")
    
height = float(input("Height of wall:"))
width = float(input("Width of wall:"))
coverage = 5

paint_calc(height=height, width=width, cover=coverage)